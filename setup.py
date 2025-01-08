from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    '''
    this will return the list of requiremnets
    '''
    requirememts-[]
    with open(file_path) as file_obj:
        requirements-file_obj.readlines()
        requirements=[req.replace("\n"."") for req in requirements]
''' -e . will be added with package names in requiremnets.txt file that will iitiates setup.py file every time. But it should not come as package into the requirement fumction here. So we need to add follwoing linw'''
        if "-e ." in requirememts:
            requirements.remove("-e .")
    return requirememts

setup(
name='mlproject',
version='0.0.1',
author='Namratha'
author_email='namratha3004@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)