<#
    FNF REMOTE - cliente
    ===================

    Roda no seu PC. Fica consultando a ponte; quando eu mando um comando,
    ele executa aqui e devolve a saida.

    NAO PRECISA INSTALAR NADA: usa so o PowerShell que ja vem no Windows.

    Como usar:
        1. deixe este arquivo na mesma pasta que "iniciar-fnf-remote.cmd"
        2. de dois cliques em "iniciar-fnf-remote.cmd"
        3. deixe a janela preta aberta

    Se voce fechar a janela, eh so dar dois cliques de novo -- ele volta a
    funcionar exatamente igual. Se quiser que abra sozinho quando ligar o PC,
    veja o LEIA-ME.

    TRAVA DE SEGURANCA (a que voce pediu):
        Este programa RECUSA executar qualquer comando que tente mexer na
        pasta System32 (ou SysWOW64, ou na pasta Windows). Nao eh aviso: ele
        nem executa, devolve codigo 99 e me explica o porque. A trava fica
        AQUI, no seu PC, antes de qualquer coisa chegar em mim.
#>

$ErrorActionPreference = 'Stop'

# ---------------------------------------------------------------- configura
# Endereco da ponte. Quem gera isso sou eu; voce nao precisa mudar.
$Ponte = $env:FNF_PONTE
if ([string]::IsNullOrWhiteSpace($Ponte)) { $Ponte = 'http://127.0.0.1:8791' }

# Senha. So este programa tem. Se ela nao bater, a ponte nao manda nada.
$Token = $env:FNF_TOKEN
if ([string]::IsNullOrWhiteSpace($Token)) {
    Write-Host 'FALTA A SENHA (FNF_TOKEN). Rode pelo "iniciar-fnf-remote.cmd".' -ForegroundColor Red
    exit 2
}
if ($Token.Length -lt 16) {
    Write-Host ('A SENHA PARECE CURTA DEMAIS ({0} caracteres).' -f $Token.Length) -ForegroundColor Red
    Write-Host 'Peca um novo "iniciar-fnf-remote.cmd" -- este nao foi gerado direito.' -ForegroundColor Red
    exit 2
}

$Intervalo = 2      # segundos entre consultas
$Teto = 2MB         # acima disso, a saida sobe em pedacos
$TetoChunk = 256KB  # tamanho de cada pedaco

[Console]::OutputEncoding = [Text.Encoding]::UTF8

# ---------------------------------------------------------------- travadura
# Padroes que este programa NUNCA executa. Comparacao sem diferenciar
# maiuscula/minuscula, e sem truque de espaco: eu tiro os espacos antes.
#
# Nota: 'system32', 'syswow64' e 'winsxs' bloqueiam sozinhos, em qualquer
# forma -- por isso NAO preciso de 'c:\windows' largo, que barraria ate um
# "Test-Path C:\Windows" inocente. O que importa eh a subpasta do sistema.
$Protegido = @(
    'system32',
    'syswow64',
    'winsxs',
    'boot.ini',
    'ntldr',
    'bootmgr',
    'pagefile.sys',
    'hiberfil.sys',
    'swapfile.sys'
)

function Test-Protegido([string]$cmd) {
    # normaliza: minusculo, sem espacos, barras trocadas -- assim
    # "S Y S T E M 3 2" ou "system 32" nao passam por um espaco.
    $n = $cmd.ToLowerInvariant()
    $n = $n -replace '\s+', ''
    $n = $n -replace '/', '\'
    foreach ($p in $Protegido) {
        if ($n.Contains($p)) { return $p }
    }
    return $null
}

# ---------------------------------------------------------------- helpers
function Send-Json([string]$rota, $obj) {
    $corpo = $obj | ConvertTo-Json -Depth 6 -Compress
    $bytes = [Text.Encoding]::UTF8.GetBytes($corpo)
    try {
        $resp = Invoke-WebRequest -Uri ($Ponte.TrimEnd('/') + $rota) `
            -Method POST -Body $bytes `
            -ContentType 'application/json; charset=utf-8' `
            -Headers @{ 'X-Token' = $Token } `
            -UseBasicParsing -TimeoutSec 30
        if ([string]::IsNullOrWhiteSpace($resp.Content)) { return $null }
        return $resp.Content | ConvertFrom-Json
    } catch {
        return $null
    }
}

function Get-Bytes([string]$caminho) {
    return [IO.File]::ReadAllBytes($caminho)
}

# ---------------------------------------------------------------- loop
Write-Host ''
Write-Host '  FNF REMOTE - cliente' -ForegroundColor Cyan
Write-Host '  ponte : ' -NoNewline; Write-Host $Ponte
Write-Host '  estado: consultando a cada ' -NoNewline; Write-Host $Intervalo -NoNewline; Write-Host ' s'
Write-Host '  trava : System32 / Windows = NUNCA executa'
Write-Host '  fechar: so feche a janela se quiser parar'
Write-Host ''

$rodando = $true
$falhas = 0

while ($rodando) {
    $r = Send-Json '/poll' @{ cliente = 'fnf-windows' }

    if ($null -eq $r) {
        $falhas++
        if ($falhas % 10 -eq 1) {
            Write-Host ("[{0:HH:mm:ss}] ponte nao responde (tentativa {1})" -f (Get-Date), $falhas) -ForegroundColor DarkYellow
        }
        Start-Sleep -Seconds $Intervalo
        continue
    }
    $falhas = 0

    if ($null -eq $r.cmd -or $r.cmd -eq '') {
        Start-Sleep -Seconds $Intervalo
        continue
    }

    $id = [int]$r.id
    $cmd = [string]$r.cmd
    $limite = 120
    if ($r.PSObject.Properties['tempo_limite']) { $limite = [int]$r.tempo_limite }

    Write-Host ("[{0:HH:mm:ss}] comando #{1}: {2}" -f (Get-Date), $id, $cmd) -ForegroundColor Green

    # ---- trava de seguranca: antes de qualquer execucao
    $atingiu = Test-Protegido $cmd
    if ($atingiu) {
        Write-Host '           RECUSADO: mexe em area protegida' -ForegroundColor Red
        Send-Json '/done' @{
            id  = $id
            rc  = 99
            out = ''
            err = ("RECUSADO PELO CLIENTE: o comando menciona '{0}', que eh area protegida "
                   + "(System32 / Windows). Nada foi executado no seu PC." -f $atingiu)
        } | Out-Null
        continue
    }

    # ---- prefixo: CMD: manda para o Prompt de Comando, o resto para o PowerShell
    $shell = 'powershell.exe'
    $arg = '-NoProfile -NonInteractive -ExecutionPolicy Bypass -Command'
    if ($cmd -match '^\s*CMD:\s*(.*)$') {
        $shell = 'cmd.exe'
        $arg = '/c'
        $cmd = $Matches[1]
    } elseif ($cmd -match '^\s*PS:\s*(.*)$') {
        $cmd = $Matches[1]
    }

    $arqOut = [IO.Path]::GetTempFileName()
    $arqErr = [IO.Path]::GetTempFileName()
    $rc = -1

    try {
        $pi = Start-Process -FilePath $shell -ArgumentList @($arg, $cmd) `
            -WorkingDirectory $env:USERPROFILE `
            -NoNewWindow -PassThru `
            -RedirectStandardOutput $arqOut -RedirectStandardError $arqErr

        $pi | Wait-Process -Timeout $limite | Out-Null
        if (-not $pi.HasExited) {
            try { $pi.Kill() } catch {}
            $rc = 124
            Add-Content -Path $arqErr -Value ("estourou o tempo limite de {0}s" -f $limite) -Encoding UTF8
        } else {
            $rc = $pi.ExitCode
        }
    } catch {
        $rc = 1
        Add-Content -Path $arqErr -Value ("$($_.Exception.GetType().Name): $($_.Exception.Message)") -Encoding UTF8
    }

    $txtOut = if (Test-Path $arqOut) { Get-Content -Raw -LiteralPath $arqOut -Encoding UTF8 } else { '' }
    $txtErr = if (Test-Path $arqErr) { Get-Content -Raw -LiteralPath $arqErr -Encoding UTF8 } else { '' }

    # ---- saida grande? sobe em pedacos e so manda a referencia
    $bOut = [Text.Encoding]::UTF8.GetBytes([string]$txtOut)
    if ($bOut.Length -gt $Teto) {
        $up = Send-Json '/chunk/start' @{ nome = ("cmd{0}.log" -f $id) }
        if ($up -and $up.upload) {
            $i = 0
            while ($i -lt $bOut.Length) {
                $n = [Math]::Min($TetoChunk, $bOut.Length - $i)
                $fatia = $bOut[$i..($i + $n - 1)]
                Send-Json '/chunk' @{ upload = $up.upload; dados = [Convert]::ToBase64String($fatia) } | Out-Null
                $i += $n
            }
            $fim = Send-Json '/chunk/finish' @{ upload = $up.upload }
            $txtOut = ("[saida grande: {0} bytes, subiu em pedacos -> {1}]" -f $bOut.Length, $fim.caminho)
        }
    }

    Write-Host ("           rc={0}, {1} bytes de saida" -f $rc, $bOut.Length) -ForegroundColor DarkGray

    Send-Json '/done' @{
        id  = $id
        rc  = $rc
        out = [string]$txtOut
        err = [string]$txtErr
    } | Out-Null

    Remove-Item -LiteralPath $arqOut, $arqErr -Force -ErrorAction SilentlyContinue
}

Write-Host 'cliente encerrado.'
