import os
from pathlib import Path

project_name = "stockPrediction"

list_of_files = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/utils.py",
    "setup.py",
    "templates/index.html",
    "requirements.txt",
    "main.py",
    "app.py",
    "Dockerfile",
    "research/trails.ipynb"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as file_obj:
            pass

    else:
        print(f"file already exists: {filepath}")