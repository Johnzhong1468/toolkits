:::: Open Jupyter Notebook in current directory

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
rem Promp the user if we cannot find Anaconda in the proper place
set /P ANACONDA_PATH="Cannot find Anaconda, please insert path to Anaconda3:"

:check_anaconda
echo AnacondaPath:%ANACONDA_PATH%

set ANACONDA_SCRIPTS_PATH="%ANACONDA_PATH%"\Scripts
set THIS_SCRIPT_DIR=%~dp0

:::: Anaconda Env Path
call %ANACONDA_SCRIPTS_PATH%\activate.bat
jupyter notebook --notebook-dir %THIS_SCRIPT_DIR%
pause