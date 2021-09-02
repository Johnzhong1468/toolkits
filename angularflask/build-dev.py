## modified from https://github.com/dmoutray/angular-flask/blob/master/build-dev.py ##

import os
import subprocess
import shutil
import time

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__)) # mod to original version, take file's path as reference
directories = os.listdir(CURRENT_DIRECTORY)
NON_ANGULAR_DIRS = ['static', 'templates', 'venv']

for directory in directories:
    if "." not in directory and directory not in NON_ANGULAR_DIRS:
        ANGULAR_PROJECT_PATH = os.path.join(CURRENT_DIRECTORY, directory)
        DIST_PATH = os.path.join(ANGULAR_PROJECT_PATH, 'dist', directory)

FLASK_STATIC_PATH = os.path.join(CURRENT_DIRECTORY, 'static')
FLASK_TEMPLATES_PATH = os.path.join(CURRENT_DIRECTORY, 'templates')

proc = subprocess.Popen(('cd ' + ANGULAR_PROJECT_PATH + ' && ng build --watch --base-href /static/ &'), shell=True)
dir_exists = True

while dir_exists & os.path.isdir(DIST_PATH):
    try:
        files = os.listdir(DIST_PATH)
        static_files = ""
        html_files = ""
        for file in files:
            if '.js' in file or '.js.map' in file or '.ico' in file or '.css' in file:
                shutil.copy(os.path.join(DIST_PATH, file), FLASK_STATIC_PATH)
            if '.html' in file:
                shutil.copy(os.path.join(DIST_PATH, file), FLASK_TEMPLATES_PATH)
        print(f"Copy Executed at {time.time()}")
    except Exception as e:
        dir_exists = False
        print(e)
    time.sleep(10.0)