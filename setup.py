from setuptools import find_packages,setup
from typing import List

Hypen_E_dot='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open('requirements.txt', 'r') as file:
        install_requires = [line.strip() for line in file]


        if Hypen_E_dot in requirements:
            requirements.remove(Hypen_E_dot)

    return requirements
        
setup(
name='mlproject',
version='0.0.1',
author='KTG',
author_email='kevintom1995@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)