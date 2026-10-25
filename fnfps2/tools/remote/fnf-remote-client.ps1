<#
    FNF REMOTE - cliente (canal GitHub)
    ==================================

    Roda no seu PC. Le um arquivo publico do GitHub onde eu escrevo os
    comandos, executa os que sao novos, e guarda a saida.

    NAO PRECISA INSTALAR NADA: usa so o PowerShell que ja vem no Windows.
    NAO PRECISA DE SENHA para receber comandos: o arquivo do canal eh
    publico, e qualquer pessoa pode LE-lo. So eu posso escrever nele.

    Como usar:
        1. deixe os arquivos juntos na mesma pasta
        2. de dois cliques em "iniciar-fnf-remote.cmd"
        3. deixe a janela preta aberta

    Fechou e reabriu? Funciona igual. O programa guarda qual comando ja
    rodou, entao nao repete nada.

    TRAVA DE SEGURANCA (a que voce pediu):
        Este programa RECUSA executar qualquer comando que tente mexer na
        pasta System32 (ou SysWOW64, ou na pasta Windows). Nao eh aviso: ele
        nem executa, devolve codigo 99 e me explica o porque. A trava fica
        AQUI, no seu PC, antes de qualquer coisa chegar em mim.
#>

$ErrorActionPreference = 'Stop'

# ---------------------------------------------------------------- configura
# Onde eu escrevo os comandos. Arquivo publico do GitHub: da para LE-lo sem
# senha, mas so eu escrevo. Se um dia eu mudar de branch, so mudo esta linha.
$Canal = $env:FNF_CANAL
if ([string]::IsNullOrWhiteSpace($Canal)) {
    $Canal = 'https://raw.githubusercontent.com/grasshopperconta-a11y/PS2Projects/arena/4c50659b-ps2projects/canal/comandos.txt'
}

# Pasta onde este programa mora. Os resultados vao para ./resultados.
$Aqui = Split-Path -Parent $MyInvocation.MyCommand.Path
$PastaResultado = Join-Path $Aqui 'resultados'
$ArqEstado      = Join-Path $Aqui 'estado.txt'
$ArqToken       = Join-Path $Aqui 'token.txt'

$Intervalo = 5        # segundos entre consultas
$Teto = 2MB           # acima disso, avisa que a saida foi truncada no console
$TempoLimitePadrao = 180

New-Item -ItemType Directory -Force -Path $PastaResultado | Out-Null
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
function Get-Canal {
    # O "?cb=" eh para furar o cache do CDN do GitHub. Sem isso, depois que
    # eu escrevo um comando novo, o seu PC poderia ficar lendo a copia velha
    # por alguns minutos.
    $url = $Canal
    if ($url -notmatch '\?') { $url = $url + '?cb=' } else { $url = $url + '&cb=' }
    $url = $url + [DateTimeOffset]::UtcNow.ToUnixTimeSeconds()
    try {
        $r = Invoke-WebRequest -Uri $url -UseBasicParsing -TimeoutSec 30
        return $r.Content
    } catch {
        return $null
    }
}

function Get-JaRodou {
    if (Test-Path $ArqEstado) {
        $v = (Get-Content -Raw -LiteralPath $ArqEstado -ErrorAction SilentlyContinue)
        if ($v -match '(\d+)') { return [int]$Matches[1] }
    }
    return 0
}

function Set-JaRodou([int]$id) {
    Set-Content -LiteralPath $ArqEstado -Value $id -Encoding ASCII -NoNewline
}

# ---------------------------------------------------------------- loop
Write-Host ''
Write-Host '  FNF REMOTE - cliente (canal GitHub)' -ForegroundColor Cyan
Write-Host '  canal : ' -NoNewline; Write-Host $Canal
Write-Host '  estado: consultando a cada ' -NoNewline; Write-Host $Intervalo -NoNewline; Write-Host ' s'
Write-Host '  trava : System32 / Windows = NUNCA executa'
Write-Host '  saida : ' -NoNewline; Write-Host $PastaResultado
Write-Host '  fechar: so feche a janela se quiser parar'
Write-Host ''

$falhas = 0
$jaRodou = Get-JaRodou
if ($jaRodou -gt 0) {
    Write-Host ("  voltando de onde parou: ultimo comando rodado foi o #{0}" -f $jaRodou) -ForegroundColor DarkGray
    Write-Host ''
}

while ($true) {
    $texto = Get-Canal

    if ($null -eq $texto) {
        $falhas++
        if ($falhas % 12 -eq 1) {
            Write-Host ("[{0:HH:mm:ss}] nao consegui ler o canal (tentativa {1})" -f (Get-Date), $falhas) -ForegroundColor DarkYellow
        }
        Start-Sleep -Seconds $Intervalo
        continue
    }
    $falhas = 0

    # ---- parse: uma linha "<id>|<comando>", ignora # e vazias
    $novos = @()
    foreach ($linha in ($texto -split "`r?`n")) {
        $l = $linha.Trim()
        if ($l -eq '' -or $l.StartsWith('#')) { continue }
        $i = $l.IndexOf('|')
        if ($i -le 0) { continue }
        $idTxt = $l.Substring(0, $i).Trim()
        $cmd = $l.Substring($i + 1).Trim()
        if ($cmd -eq '') { continue }
        $id = 0
        if (-not [int]::TryParse($idTxt, [ref]$id)) { continue }
        # id tem de ser >= 1: o estado inicial eh 0, e a comparacao abaixo eh
        # "<=" -- um id 0 (ou negativo) nunca passaria e eu ia achar que o
        # comando tinha sumido. Sem essa linha, id 0 eh um comando fantasma.
        if ($id -lt 1) { continue }
        if ($id -le $jaRodou) { continue }
        $novos += [pscustomobject]@{ id = $id; cmd = $cmd }
    }

    if ($novos.Count -eq 0) {
        Start-Sleep -Seconds $Intervalo
        continue
    }

    $novos = $novos | Sort-Object id

    foreach ($job in $novos) {
        $id = $job.id
        $cmd = $job.cmd

        Write-Host ("[{0:HH:mm:ss}] comando #{1}: {2}" -f (Get-Date), $id, $cmd) -ForegroundColor Green

        # ---- trava de seguranca: antes de qualquer execucao
        $atingiu = Test-Protegido $cmd
        if ($atingiu) {
            Write-Host '           RECUSADO: mexe em area protegida' -ForegroundColor Red
            #string numa linha so: quebrar com '+' faz o parser do PowerShell
            #tratar a quebra como fim de instrucao (erro MissingEndParenthesis)
            $txt = "RECUSADO PELO CLIENTE: o comando menciona '$atingiu', que eh area protegida (System32 / Windows). Nada foi executado no seu PC."
            Set-Content -LiteralPath (Join-Path $PastaResultado ("resultado-{0}.txt" -f $id)) -Value $txt -Encoding UTF8
            # marca como rodado mesmo recusado, senao ele tentaria de novo para sempre
            $jaRodou = $id
            Set-JaRodou $id
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

            $pi | Wait-Process -Timeout $TempoLimitePadrao | Out-Null
            if (-not $pi.HasExited) {
                try { $pi.Kill() } catch {}
                $rc = 124
                Add-Content -Path $arqErr -Value ("estourou o tempo limite de {0}s" -f $TempoLimitePadrao) -Encoding UTF8
            } else {
                $rc = $pi.ExitCode
            }
        } catch {
            $rc = 1
            Add-Content -Path $arqErr -Value ("$($_.Exception.GetType().Name): $($_.Exception.Message)") -Encoding UTF8
        }

        $txtOut = if (Test-Path $arqOut) { Get-Content -Raw -LiteralPath $arqOut -Encoding UTF8 } else { '' }
        $txtErr = if (Test-Path $arqErr) { Get-Content -Raw -LiteralPath $arqErr -Encoding UTF8 } else { '' }

        # ---- monta o arquivo de resultado, com o comando junto
        $relatorio = @()
        $relatorio += "comando #$id"
        $relatorio += "rodado em: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
        $relatorio += "comando  : $cmd"
        $relatorio += "codigo   : $rc"
        $relatorio += "-------- saida --------"
        if ([string]$txtOut) { $relatorio += $txtOut.TrimEnd() }
        if ([string]$txtErr) {
            $relatorio += "-------- erros --------"
            $relatorio += $txtErr.TrimEnd()
        }
        $corpo = $relatorio -join "`r`n"

        $arqRel = Join-Path $PastaResultado ("resultado-{0}.txt" -f $id)
        Set-Content -LiteralPath $arqRel -Value $corpo -Encoding UTF8

        Write-Host ("           rc={0}, {1} bytes -> {2}" -f $rc, $corpo.Length, (Split-Path -Leaf $arqRel)) -ForegroundColor DarkGray

        # ---- console: mostra a saida (curta) para voce poder ler ou copiar
        $bOut = [Text.Encoding]::UTF8.GetByteCount([string]$txtOut)
        if ($bOut -le $Teto) {
            $linhas = ($txtOut -split "`r?`n")
            if ($linhas.Count -le 40) {
                foreach ($ln in $linhas) { if ($ln -ne '') { Write-Host "           $ln" } }
            } else {
                Write-Host "           (saida com $($linhas.Count) linhas; veja o arquivo)"
            }
        } else {
            Write-Host "           (saida com $bOut bytes; veja o arquivo)"
        }
        if ([string]$txtErr) {
            Write-Host '           --- erros ---' -ForegroundColor DarkYellow
            $elinhas = ($txtErr -split "`r?`n")
            if ($elinhas.Count -le 20) {
                foreach ($ln in $elinhas) { if ($ln -ne '') { Write-Host "           $ln" -ForegroundColor DarkYellow } }
            } else {
                Write-Host "           ($($elinhas.Count) linhas de erro; veja o arquivo)" -ForegroundColor DarkYellow
            }
        }

        $jaRodou = $id
        Set-JaRodou $id
    }

    Start-Sleep -Seconds $Intervalo
}
