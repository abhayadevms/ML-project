from setuptools import find_packages, setup
from typing import List


HYPEN_DOT ="-e ."
def get_requirements(file_path: str = "requirements.txt") -> List[str]:
    """read the reuirment.txt and data convert to list"""

    datas = []
    with open(file_path) as file :
        datas = file.readlines()
        datas = [data.replace('\n',"") for data in datas]

        if HYPEN_DOT in datas:
            datas.remove(HYPEN_DOT)
    return datas




setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'abhayadev',
    author_email='mail.abhayadev@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt"),
)