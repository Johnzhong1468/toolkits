## Conda & python
* crate conda env: <br>
conda create -n env_name python=3.10
* conda create from file: <br>
conda env create -f "%FOLDER_ROOT%%ENV_NAME%.yml"
* pip upgrade: <br>
python -m pip install --upgrade pip
* pip install requirements: <br>
pip install -r requirements.txt
* conda update: <br>
conda update -n base -c defaults conda