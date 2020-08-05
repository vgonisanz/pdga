import os
import pathlib

from setuptools import setup, find_packages

ROOT_PATH = pathlib.Path(__file__).parent
README = (ROOT_PATH / "README.md").read_text()

SCRIPTS_PATH = os.path.join("pdga", "samples")
SCRIPTS_LIST = [os.path.join(SCRIPTS_PATH, f) for f in os.listdir(SCRIPTS_PATH) if os.path.isfile(os.path.join(SCRIPTS_PATH, f))]

# Requirements
def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

install_reqs = parse_requirements('requirements.txt')

# Package generation
setup(
    name="pdga",
    version="0.1.0",
    description="Procedural Dungeon Generation Algorithm",
    long_description=README,
    long_description_content_type="text/markdown",
    keywords='Procedural Dungeon Generation Algorithm',
    url="https://github.com/vgonisanz/pdga",
    author="vgonisanz",
    author_email="vgonisanz@gmail.com",
    license="GPLv3+",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["pdga"],
    include_package_data=True,
    install_requires=install_reqs
)
# packages=["pdga", "pdga/scripts"],    
#find_packages(include=['pdga', 'pdga/scripts/.*']),