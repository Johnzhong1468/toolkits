title toolkit env setup

call %~dp0\..\scripts\set_up_anaconda.bat

call %ANACONDA_SCRIPTS_PATH%\activate.bat "%ANACONDA_PATH%"
if %ERRORLEVEL% neq 0 (
    echo Error calling activate.bat, something wrong with anaconda set up
    goto end
)

set ENV_NAME=toolkit
set FOLDER_ROOT=%~dp0

call conda info
call conda activate toolkit

if %ERRORLEVEL% neq 0 (
    echo creating %ENV_NAME% env from %FOLDER_ROOT%%ENV_NAME%.yml
    call conda env create -f "%FOLDER_ROOT%%ENV_NAME%.yml"
    goto post_install
)

echo env exists, update env
conda env update -f "%FOLDER_ROOT%%ENV_NAME%.yml"

:post_install
if %ERRORLEVEL% neq 0 (
    echo error creating conda environment
    goto end
)

call mkdir %FOLDER_ROOT%..\temp
call mkdir %FOLDER_ROOT%..\logs

:end
pause
