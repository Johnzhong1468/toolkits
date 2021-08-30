:::: Open Jupyter Notebook in current directory
set TARGET_DIR=%~dp0

:::: Anaconda Env Path
call "C:\Users\0429z\Anaconda3\Scripts\activate.bat"
jupyter notebook --notebook-dir %TARGET_DIR%