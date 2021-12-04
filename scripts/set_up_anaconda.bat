:::: Set up anaconda path

@echo off

if exist "%HOMEDRIVE%%HOMEPATH%\Anaconda3" (
    set "ANACONDA_PATH=%HOMEDRIVE%%HOMEPATH%\Anaconda3"
    goto check_anaconda
)
if exist "%HOMEDRIVE%%HOMEPATH%\AppData\Local\Continuum\Anaconda3" (
    set "ANACONDA_PATH=%HOMEDRIVE%%HOMEPATH%\AppData\Local\Continuum\Anaconda3"
    goto check_anaconda
)
if exist  "%HOMEDRIVE%\ProgramData\Anaconda3\" (
    set "ANACONDA_PATH=%HOMEDRIVE%\ProgramData\Anaconda3"
    goto check_anaconda
)
if exist  "%HOMEDRIVE%\Program Files\Anaconda3\" (
    set "ANACONDA_PATH=%HOMEDRIVE%\Program Files\Anaconda3"
    goto check_anaconda
)
rem Prompt the user if we cannot find Anaconda in the proper place
set /P ANACONDA_PATH="Cannot find Anaconda, please insert path to Anaconda3:"

:check_anaconda
echo AnacondaPath:%ANACONDA_PATH%

set ANACONDA_SCRIPTS_PATH="%ANACONDA_PATH%"\Scripts
