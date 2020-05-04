import io
import os

from setuptools import setup, find_packages

setup(
    name="python_eye",
    version="0.0.1dev1",
    author="Denys Iaremenko",
    author_email="denysiaremenko@gmail.com",
    description="A package for Automation that compare two images and return if there is a difference between them",
    long_description=io.open(os.path.join(os.path.dirname("__file__"), "README.md"), encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Environment :: Console",
        "Environment :: MacOS X",
        "Intended Audience :: Developers",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing"
    ],
    keywords=[
        "image difference",
        "image comparison"
        "appium",
        "selenium",
        "automation",
        "ui validation"
    ],
    python_requires=">=3.6",
    install_requires=[
        "opencv-python==4.2.0.34",
        "pytest==5.4.1",
        "loguru==0.4.1",
    ]
)