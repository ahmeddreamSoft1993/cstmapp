from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in cstmapp/__init__.py
from cstmapp import __version__ as version

setup(
	name="cstmapp",
	version=version,
	description="this is my cstmapp",
	author="ahmed",
	author_email="ahmedgn1993@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
