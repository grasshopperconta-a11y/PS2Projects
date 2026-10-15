@echo off
REM ===========================================================================
REM  COMPILAR.bat -- um clique: compila, confere os assets e copia pro pendrive
REM ===========================================================================
REM
REM  Duplo-clique, ou num terminal:
REM
REM      COMPILAR.bat
REM
REM  O que ele faz, em ordem:
REM    1. acha o WSL (o Linux dentro do Windows)
REM    2. traduz o caminho da pasta para o Linux
REM    3. confere se tem gcc, make e python3 la dentro
REM    4. acha o ps2sdk
REM    5. compila -- la dentro, no disco do Linux, nao no /mnt/c
REM    6. confere os 16 assets de runtime
REM    7. copia tudao pro pendrive
REM
REM  Opcoes:
REM     COMPILAR.bat --instalar-ps2sdk   instala o ps2sdk no WSL (demora ~1h)
REM     COMPILAR.bat --so-compilar       para no passo 5, nao copia
REM     COMPILAR.bat --so-assets         so confere os assets
REM     COMPILAR.bat --limpar            apaga objetos e saida, comeca do zero
REM     COMPILAR.bat --rapido            -O1 em vez de -O2, itera mais rapido
REM     COMPILAR.bat --distro=NOME       forca uma distro WSL especifica
REM     COMPILAR.bat --ps2dev=/caminho   diz onde o ps2sdk esta'
REM     COMPILAR.bat --ajuda             a lista completa
REM
REM  DUAS COISAS QUE PARECEM BUG MAS SAO DECISAO:
REM
REM  * Este .bat NAO compila nativo no Windows, e nao ha' como. O ps2sdk usa
REM    autotools, Makefiles POSIX e shell script -- nada disso existe no
REM    cmd.exe. No Windows o caminho suportado eh o WSL. O .bat so' traduz:
REM    detecta o WSL, roda o build de verdade la' dentro, e cuida da parte que
REM    eh do Windows (letra do pendrive, copiar arquivo). Toda a logica fica em
REM    build.sh, que eh o mesmo arquivo nos dois sistemas.
REM
REM  * Ele NAO lista as distros com "wsl -l -q". Esse comando cospe a saida em
REM    UTF-16, e o for /f do cmd.exe le como texto: "Ubuntu-22.04" vira
REM    U\0b\0u\0... e so' o "U" sobrevive. A versao anterior deste script fazia
REM    exatamente isso e concluia que a distro se chamava "U". Em vez de
REM    adivinhar a distro, usamos o wsl puro, que roda a padrao -- que eh a
REM    quase sempre a certa. Quem tem mais de uma passa --distro=NOME.
REM ===========================================================================

setlocal EnableDelayedExpansion
cd /d "%~dp0"

set "HERE=%~dp0"
set "HERE=%HERE:~0,-1%"
set "WSLPATH="
set "PS2DEV="
set "EXTRA="
set "DO_COPY=1"
set "DO_TOOLCHAIN=0"
set "DO_ASSETS_ONLY=0"

REM ---------------------------------------------------------------- arguments

for %%A in (%*) do (
    if /i "%%~A"=="--instalar-ps2sdk" set "DO_TOOLCHAIN=1"
    if /i "%%~A"=="--so-compilar"    set "DO_COPY=0"
    if /i "%%~A"=="--so-assets"      set "DO_ASSETS_ONLY=1"
    if /i "%%~A"=="--limpar"         set "EXTRA=!EXTRA! --clean"
    if /i "%%~A"=="--rapido"         set "EXTRA=!EXTRA! --fast"
    if /i "%%~A"=="--ajuda"          goto :help
    for /f "tokens=1,2 delims==" %%X in ("%%~A") do (
        if /i "%%~X"=="--ps2dev" set "PS2DEV=%%~Y"
        if /i "%%~X"=="--distro" set "DISTRO_OVERRIDE=%%~Y"
    )
)

REM ------------------------------------------------------------------- header

echo.
echo ============================================================
echo   FNF PS2 -- compilar e copiar pro pendrive
echo ============================================================
echo.
echo   Pasta: %HERE%
echo.

REM ------------------------------------------------------------- 1. find WSL

echo [1/7] Procurando o WSL...

REM wsl.exe vive no System32, que quase sempre esta' no PATH -- mas nao
REM sempre. Um PATH enxuto, ou alguns launchers, o perdem, e a conclusao
REM errada "nao tem WSL" sai da mesma. Tenta o caminho explicito antes.
set "WSL="
where wsl.exe >nul 2>&1 && set "WSL=wsl.exe"
if not defined WSL if exist "%SystemRoot%\System32\wsl.exe" set "WSL=%SystemRoot%\System32\wsl.exe"
if not defined WSL if exist "%SystemRoot%\Sysnative\wsl.exe" set "WSL=%SystemRoot%\Sysnative\wsl.exe"
if not defined WSL goto :no_wsl

REM WSL ganhou -e ("roda isto, nao passa por um shell de login"); builds
REM antigos nao tem. Um que nao conhece -e falha no meio do make com erro de
REM comando, nao de flag. Testa uma vez, aqui, onde o erro eh obvio.
set "WSLEX="
"%WSL%" -e echo wslok >nul 2>&1 && set "WSLEX=-e"

if defined DISTRO_OVERRIDE (
    set "WSLRUN="%WSL%" -d !DISTRO_OVERRIDE!"
    echo       OK, distro: !DISTRO_OVERRIDE!
) else (
    set "WSLRUN="%WSL%""
    echo       OK, vou usar a distro padrao do WSL
)

if "%DO_TOOLCHAIN%"=="1" goto :install_toolchain

REM ------------------------------------------- 2. windows path -> linux path

echo [2/7] Traduzindo o caminho para o Linux...
REM C:\Users\eu\x  ->  /mnt/c/Users/eu/x
set "WP=%HERE%"
set "DRIVE=!WP:~0,1!"
set "REST=!WP:~2!"
set "REST=!REST:\=/!"
for %%L in (a b c d e f g h i j k l m n o p q r s t u v w x y z) do (
    if /i "!DRIVE!"=="%%L" set "DRIVE=%%L"
)
set "WSLPATH=/mnt/!DRIVE!!REST!"
if not exist "%HERE%\build.sh" (
    echo.
    echo   ERRO: nao achei build.sh em %HERE%
    echo   Extraia o FNFPS2-0.2.105.tar.gz primeiro.
    echo.
    pause & exit /b 1
)
echo       OK: !WSLPATH!

REM Confirma de dentro do WSL que ele realmente ve a pasta. Sem isso, um
REM caminho que o Linux nao enxerga so' aparece como "build.sh nao encontrado"
REM la' no passo 5, muito depois de ter perdido tempo.
!WSLRUN! !WSLEX! sh -c "test -f '!WSLPATH!/build.sh'" >nul 2>&1
if errorlevel 1 (
    echo.
    echo   ERRO: o WSL nao esta' conseguindo ver a pasta.
    echo   Esperava encontrar build.sh em !WSLPATH!
    echo.
    echo   Se o projeto esta' em outra unidade ^(D:, E:...^), o /mnt/ so'
    echo   cobre as que o WSL monta. Rode no Ubuntu:
    echo       sudo mkdir -p /mnt/d ^&^& sudo mount -t drvfs D: /mnt/d
    echo.
    pause & exit /b 1
)

REM ---------------------------------------- 3. gcc / make / python3 no WSL

echo [3/7] Conferindo gcc, make e python3 no WSL...
!WSLRUN! !WSLEX! sh -c "command -v gcc >/dev/null && command -v make >/dev/null && command -v python3 >/dev/null" >nul 2>&1
if errorlevel 1 (
    echo.
    echo   Faltam ferramentas basicas. Instalando...
    echo   ^(vai pedir a sua senha de usuario do Ubuntu^)
    echo.
    !WSLRUN! !WSLEX! sudo sh -c "apt-get update && apt-get install -y build-essential python3 git"
    if errorlevel 1 (
        echo.
        echo   ERRO: nao consegui instalar. Rode num terminal Ubuntu:
        echo       sudo apt-get install -y build-essential python3 git
        echo.
        pause & exit /b 1
    )
)
echo       OK.

REM --------------------------------------------- 4. achar o ps2sdk no WSL

echo [4/7] Procurando o ps2sdk...
set "FOUND="
REM A busca roda dentro de um script, nao num laco aqui. Duas razoes:
REM
REM  1. Um laco batch com set dentro de bloco eh onde nasceu o
REM     "set foi inesperado neste momento".
REM
REM  2. NAO da' para capturar a saida com for /f direto:
REM        for /f "usebackq ..." %%P in (`!WSLRUN! ... sh "..."`) do ...
REM     O comando entre backquotes contem aspas, e o parser do cmd.exe se
REM     perde nelas -- ele tratou a linha inteira como texto e tentou
REM     executar 'wsl.exe" -e sh "', que nao existe. Passos 1 a 3 funcionam
REM     porque sao linha de comando normal; so' o que esta' dentro de um
REM     for /f quebra.
REM
REM  O padrao seguro: manda a saida para um arquivo, e le o arquivo. Com
REM  usebackq, aspas duplas significam "nome de arquivo", entao nao ha'
REM  comando a interpretar -- e linhas em branco sao puladas sozinhas, o que
REM  tambem resolve o caso de nao achar nada.
set "FOUND="
!WSLRUN! !WSLEX! sh "!WSLPATH!/tools/find_ps2dev.sh" > "%TEMP%\fnf-ps2dev.txt" 2>nul
if exist "%TEMP%\fnf-ps2dev.txt" (
    for /f "usebackq tokens=*" %%P in ("%TEMP%\fnf-ps2dev.txt") do set "FOUND=%%P"
    del "%TEMP%\fnf-ps2dev.txt" >nul 2>&1
)

if defined FOUND (
    echo       OK, achei em !FOUND!
    set "PS2DEV=!FOUND!"
) else (
    echo.
    echo   NAO ACHEI O PS2SDK.
    echo.
    echo   Se ele ja' esta' instalado em outro lugar, me diga onde:
    echo       COMPILAR.bat --ps2dev=/caminho/para/ps2dev
    echo.
    echo   Se ainda nao tem, eu instalo agora ^(demora mais ou menos 1 hora^):
    echo       COMPILAR.bat --instalar-ps2sdk
    echo.
    pause & exit /b 1
)

REM ------------------------------------------------------------ 5. compilar

echo.
echo [5/7] Compilando...
echo.

if "%DO_ASSETS_ONLY%"=="1" (
    !WSLRUN! !WSLEX! sh -c "cd '!WSLPATH!' && PS2DEV='!PS2DEV!' ./build.sh --check-assets !EXTRA!"
    echo.
    echo   Abrindo a lista de links no seu navegador...
    echo   Baixe cada arquivo e mova para:  %HERE%\assets\
    echo.
    if exist "%HERE%\assets-faltando.html" start "" "%HERE%\assets-faltando.html"
    goto :fim
)

REM Compila no disco do Linux, nao no /mnt/c. O /mnt/c eh um sistema de
REM arquivos de rede do ponto de vista do Linux: cada stat, cada open, cada
REM write cruza para o Windows e volta. Um build de PS2 toca algumas centenas
REM de arquivos varias vezes, entao compilar ali eh minutos em vez de segundos
REM -- e piora a medida que a arvore cresce. tools/wsl-run.sh copia a arvore
REM para la', compila, e traz de volta so' o que interessa.
!WSLRUN! !WSLEX! sh "!WSLPATH!/tools/wsl-run.sh" "!WSLPATH!" "!PS2DEV!" --deploy !EXTRA!
if errorlevel 1 (
    echo.
    echo ============================================================
    echo   O BUILD FALHOU.
    echo ============================================================
    echo.
    echo   O log completo esta' em:
    echo       %HERE%\build.log
    echo.
    echo   Me manda esse arquivo que eu resolvo.
    echo.
    pause & exit /b 1
)

if not exist "%HERE%\build\ps2\FNFPS2\assets\audio_stems.pcm" (
    echo.
    echo   ------------------------------------------------------------
    echo   FALTAM ASSETS. Sem eles o ELF compila mas nao passa da
    echo   primeira leitura de arquivo no console.
    echo   ------------------------------------------------------------
    echo.
    echo   Abrindo a lista de links no seu navegador...
    echo   Baixe cada arquivo e mova para:  %HERE%\assets\
    echo   Depois rode COMPILAR.bat de novo.
    echo.
    if exist "%HERE%\assets-faltando.html" start "" "%HERE%\assets-faltando.html"
    pause & exit /b 1
)

if "%DO_COPY%"=="0" (
    echo.
    echo   Pronto. saida em %HERE%\build\ps2\FNFPS2\
    echo.
    pause & exit /b 0
)

REM ------------------------------------------------- 6. copiar pro pendrive

echo [6/7] Procurando o pendrive...
set "PEN="
REM Mesma historia do ps2dev: PowerShell com aspas dentro de um for /f
REM backquotado quebra do mesmo jeito. Saida para arquivo, depois le.
powershell -NoProfile -Command "Get-CimInstance Win32_LogicalDisk -Filter 'DriveType=2' ^| Select-Object -ExpandProperty DeviceID" > "%TEMP%\fnf-pen.txt" 2>nul
if exist "%TEMP%\fnf-pen.txt" (
    for /f "usebackq tokens=*" %%D in ("%TEMP%\fnf-pen.txt") do (
        if not defined PEN set "PEN=%%D"
    )
    del "%TEMP%\fnf-pen.txt" >nul 2>&1
)

if not defined PEN (
    echo.
    echo   Nao achei pendrive encaixado.
    echo   A saida esta' pronta em: %HERE%\build\ps2\FNFPS2\
    echo   Copie essa pasta para o pendrive como  FNFPS2\
    echo   ^(ou seja: X:\FNFPS2\fnf_ps2_m84.elf^)
    echo.
    pause & exit /b 0
)

echo       Achei: !PEN!
echo.
echo   Vou copiar para !PEN!\FNFPS2\
echo   Isso sobrescreve o que estiver la.
echo.
choice /c SN /m "Confirma"
if errorlevel 2 (
    echo   Cancelado. A saida esta' em %HERE%\build\ps2\FNFPS2\
    pause & exit /b 0
)

echo.
echo [7/7] Copiando...
if exist "!PEN!\FNFPS2" rd /s /q "!PEN!\FNFPS2" >nul 2>&1
xcopy "%HERE%\build\ps2\FNFPS2" "!PEN!\FNFPS2\" /e /i /q /y >nul
if errorlevel 1 (
    echo   ERRO na copia. Tente na mao:
    echo       xcopy "%HERE%\build\ps2\FNFPS2" "!PEN!\FNFPS2\" /e /i /y
    pause & exit /b 1
)

echo.
echo ============================================================
echo   PRONTO. Ta' no pendrive.
echo ============================================================
echo.
echo   !PEN!\FNFPS2\fnf_ps2_m84.elf
echo   !PEN!\FNFPS2\assets\          ^(16 arquivos^)
echo   !PEN!\FNFPS2\assets\songs\   ^(81 charts^)
echo.
echo   No PS2, abra pelo uLaunchELF em mc0: ou mass:
echo.
pause
exit /b 0

REM ------------------------------------------------------------------ helpers

:no_wsl
echo.
echo ============================================================
echo   PRECISO DO WSL ^(o Linux dentro do Windows^)
echo ============================================================
echo.
echo   O ps2sdk nao compila nativo no Windows -- o build dele usa
echo   shell script e autotools, que so' existem no Linux. No Windows
echo   o caminho suportado eh o WSL, que jah vem no Windows 10/11.
echo.
echo   Para instalar, abra o PowerShell COMO ADMINISTRADOR e rode:
echo.
echo       wsl --install
echo.
echo   Reinicie o PC quando terminar, volte aqui e rode de novo.
echo   Ele instala o Ubuntu sozinho e pede para criar usuario/senha.
echo.
pause
exit /b 1

:install_toolchain
echo.
echo ============================================================
echo   INSTALANDO O PS2SDK NO WSL
echo ============================================================
echo.
echo   Isso demora mais ou menos 1 hora e precisa de uns 6 GB livres.
echo   Vai pedir sua senha de usuario do Ubuntu varias vezes.
echo.
choice /c SN /m "Comecar agora"
if errorlevel 2 exit /b 0
echo.

!WSLRUN! !WSLEX! sh -c "sudo apt-get update && sudo apt-get install -y build-essential python3 git texinfo flex bison m4 autoconf automake libtool cmake libgmp-dev libmpfr-dev libmpc-dev zlib1g-dev"
if errorlevel 1 (
    echo   ERRO instalando dependencias. Veja acima.
    pause & exit /b 1
)

echo.
echo   Baixando e compilando o ps2toolchain...
echo   ^(pode ir tomar um cafe'^)
echo.
!WSLRUN! !WSLEX! sh -c "git clone --depth=1 https://github.com/ps2dev/ps2toolchain ~/ps2toolchain 2>/dev/null; cd ~/ps2toolchain && ./build-all.sh"
if errorlevel 1 (
    echo.
    echo   ERRO no build do ps2toolchain. Me mande a saida acima.
    pause & exit /b 1
)

echo.
echo ============================================================
echo   PS2SDK INSTALADO em  /home/seu-usuario/ps2dev
echo ============================================================
echo   Agora eh so' rodar:  COMPILAR.bat
echo.
pause
exit /b 0

:help
type "%~f0" | findstr /r "^REM  " | more +5
exit /b 0

:fim
echo.
pause
exit /b 0
