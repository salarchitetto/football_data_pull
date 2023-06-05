from setuptools import find_packages, setup

setup(
    name="Football Data Pull",
    version="0.0.1",
    author="Salvatore Architetto",
    author_email="footydash.io@gmail.com",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["setuptools", "wheel"],
)