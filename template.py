import os
from pathlib import Path
import logging

# This script sets up the how logging information will be displayed
logging.basicConfig(level= logging.INFO, format='%(asctime)s : %(levelname)s : %(message)s')


project_name = "SatuSure_CS"


# list of files and folder for setting up project
list_of_files= [
  ".github/workflow/main.yaml",
  f"src/{project_name}/__init__.py",
  f"src/{project_name}/components/__init__.py",
  f"src/{project_name}/utils/__init__.py",
  f"src/{project_name}/config/__init__.py",
  f"src/{project_name}/pipeline/__init__.py",
  f"src/{project_name}/entity/__init__.py",
  f"src/{project_name}/constants/__init__.py",
  "config/config.yaml",
  "params.yaml",
  "requirements.txt",
  "setup.py",
  "main.py",
  "app.py",
  "test.py",
  "research/stage_01.ipynb"
  "research/stage_02.ipynb"
  "research/stage_03.ipynb"
  "research/stage_04.ipynb"
  "research/stage_05.ipynb"
]


# Create directories and files if they do not exist
# If the directory does not exist, it will be created
# If the file does not exist, it will be created as an empty file
for filepath in list_of_files:
  filepath = Path(filepath)
  filedir,filename = os.path.split(filepath)

  # Create the directory if it does not exist
  if filedir != "":
    os.makedirs(filedir, exist_ok=True)
    logging.info(f"creating directory:{filedir} for file: {filename}")


  # Check if the file exists and is not empty
  if(not os.path.exists(filepath)) or (os.path.getsize(filepath== 0)):
    with open(filepath, 'w') as f:
      pass #creating an empty file
      logging.info(f"creating empty file:{filepath}")


  else:
    logging.info(f"{filename} already exist")