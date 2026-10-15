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
REM    2. confere se tem gcc, make e python3 la dentro
REM    3. acha o ps2sdk (ou oferece instalar)
REM    4. compila o ELF do PS2
REM    5. confere se os 16 assets de runtime estao todos la
REM    6. copia tudao pro pendrive
REM
REM  Opcoes:
REM     COMPILAR.bat --instalar-ps2sdk   instala o ps2sdk no WSL (demora ~1h)
REM     COMPILAR.bat --so-compilar       para no passo 4, nao copia
REM     COMPILAR.bat --so-assets         so confere os assets
REM     COMPILAR.bat --limpar            apaga objetos e saida, comeca do zero
REM     COMPILAR.bat --rapido            -O1 em vez de -O2, itera mais rapido
REM     COMPILAR.bat --distro=NOME       forca uma distro WSL especifica
REM     COMPILAR.bat --ps2dev=/caminho   diz onde o ps2sdk esta'
REM     COMPILAR.bat --ajuda             a lista completa
REM
REM  POR QUE WSL: o ps2sdk nao compila nativo no Windows. O build dele usa
REM  autotools, Makefiles POSIX e shell script -- nao existe port para cmd.exe.
REM  No Windows o caminho suportado eh o WSL. O .bat so' traduz: detecta o WSL,
REM  roda o build de verdade (build.sh) la' dentro, e cuida da parte que eh
REM  do Windows (letra do pendrive, copiar arquivo).
REM ===========================================================================

setlocal EnableDelayedExpansion
cd /d "%~dp0"

set "HERE=%~dp0"
set "HERE=%HERE:~0,-1%"
set "DISTRO="
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
    )
    for /f "tokens=1,2 delims==" %%X in ("%%~A") do (
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

echo [1/6] Procurando o WSL...

REM wsl.exe lives in System32, which is almost always on PATH -- but not
REM always: a stripped-down PATH, or some launchers, lose it. Try the explicit
REM paths before concluding WSL is absent.
set "WSL="
where wsl.exe >nul 2>&1 && set "WSL=wsl.exe"
if not defined WSL if exist "%SystemRoot%\System32\wsl.exe" set "WSL=%SystemRoot%\System32\wsl.exe"
if not defined WSL if exist "%SystemRoot%\Sysnative\wsl.exe" set "WSL=%SystemRoot%\Sysnative\wsl.exe"
if not defined WSL goto :no_wsl

REM wsl -l -q prints ONLY the distro names, one per line, with no header. An
REM earlier version of this script used skip=1, which is right for "wsl -l"
REM but wrong for "wsl -l -q" -- with a single distro it skipped the only line
REM there was and reported WSL as missing. Filter instead of skipping: drop
REM blank lines and the localized header some builds print anyway.
set "DISTRO="
if defined DISTRO_OVERRIDE (
    set "DISTRO=!DISTRO_OVERRIDE!"
) else (
    for /f "usebackq tokens=*" %%D in (`"%WSL%" -l -q 2^>nul`) do (
        if not defined DISTRO (
            set "LINE=%%D"
            if not "!LINE!"=="" (
                echo !LINE! | findstr /i /c:"Subsystem" >nul 2>&1 || set "DISTRO=%%D"
            )
        )
    )
)
if not defined DISTRO (
    REM Enumeration came up empty. That does not mean WSL is missing -- some
    REM builds mangle "wsl -l -q" output when it is redirected. Fall back to
    REM bare wsl, which runs the default distro, rather than giving up.
    echo       ^(nao consegui listar as distros; vou usar a padrao^)
    set "WSLRUN="%WSL%""
) else (
    echo       OK, distro: !DISTRO!
    set "WSLRUN="%WSL%" -d !DISTRO!"
)

REM WSL gained -e ("run this, do not go through a login shell"); older builds do
REM not have it, and passing it to one that does not know it fails deep inside
REM the build with a confusing error. Probe once, here, where the failure is
REM obvious.
set "WSLEX="
"%WSL%" -e echo wslok >nul 2>&1 && set "WSLEX=-e"
if defined WSLEX (echo       OK, esta' distro aceita -e) else (echo       OK, distro antiga, sem -e)

if "%DO_TOOLCHAIN%"=="1" goto :install_toolchain

REM ------------------------------------------- 2. windows path -> linux path

echo [2/6] Traduzindo o caminho para o Linux...
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

echo [3/6] Conferindo gcc, make e python3 no WSL...
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

echo [4/6] Procurando o ps2sdk...
set "FOUND="
REM /usr/local/ps2dev first: that is where ps2toolchain's build-all.sh
REM installs, and it is where this user's is. %PS2DEV% is a Windows variable,
REM so it has to be handed to the shell rather than expanded by cmd.
set "CAND=%PS2DEV%"
if "!CAND!"=="" set "CAND=/usr/local/ps2dev"
for %%P in ("!CAND!" "/usr/local/ps2dev" "$HOME/ps2dev" "/opt/ps2dev" "/usr/local/ps2sdk" "/var/tmp/ps2dev-root/ps2dev") do (
    if not defined FOUND (
        !WSLRUN! !WSLEX! sh -c "test -x '%%P/bin/ee-gcc' -o -x '%%P/ee/bin/ee-gcc'" >nul 2>&1
        if not errorlevel set "FOUND=%%P"
    )
)
if defined FOUND (
    echo       OK, achei em !FOUND!
    set "PS2DEV=!FOUND!"
) else (
    echo.
    echo   NAO ACHEI O PS2SDK.
    echo.
    echo   Se ele ja' esta' instalado em outro lugar, me diga onde:
    echo       set PS2DEV=/caminho/para/ps2dev
    echo       COMPILAR.bat
    echo.
    echo   Se ainda nao tem, eu instalo agora ^(demora mais ou menos 1 hora^):
    echo       COMPILAR.bat --instalar-ps2sdk
    echo.
    pause & exit /b 1
)

REM ------------------------------------------------------- 5. compilar

echo.
echo [5/6] Compilando... ^(a primeira vez demora mais^)
echo.
echo   Uma coisa: compilar dentro de /mnt/c eh mais lento que no disco do
echo   Linux, porque o WSL acessa o Windows por cima de um sistema de arquivos
echo   de rede. Se ficar incomodo, eu mudo para copiar tudo para dentro do
echo   Ubuntu, compilar la', e trazer so' o resultado de volta.
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

!WSLRUN! !WSLEX! sh -c "cd '!WSLPATH!' && PS2DEV='!PS2DEV!' ./build.sh --deploy !EXTRA!"
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

echo [6/6] Procurando o pendrive...
set "PEN="
for /f "usebackq tokens=*" %%D in (`powershell -NoProfile -Command "Get-CimInstance Win32_LogicalDisk -Filter 'DriveType=2' ^| Select-Object -ExpandProperty DeviceID" 2^>nul`) do (
    if not defined PEN set "PEN=%%D"
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
echo   Copiando...
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
echo   Vai pedir sua senha de usuario do Ubuntu algumas vezes.
echo.
choice /c SN /m "Comecar agora"
if errorlevel 2 exit /b 0
echo.

REM WSL, the distro and WSLRUN were all resolved before this label.
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
