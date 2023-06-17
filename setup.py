from setuptools import find_packages, setup
from typing import List



HYPEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    try:

        requirements = []
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        print('requirements', requirements)
        return requirements

    except Exception as e:
        print(f'error while reading the requirements.txt {e}')


setup(
    name='teslaStockPrediction',
    version='0.0.1',
    author='kiran',
    author_email='@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    package_dir={"": "src"},
    packages=find_packages(where="src")
    
)