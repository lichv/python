# coding=utf-8

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lichv.utility",
    version="0.0.1",
    author="lichv",
    author_email="lichvy@126.com",
    description="Utility tools with mongodb,mysqldb,sms,semail,brower",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lichv/python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)