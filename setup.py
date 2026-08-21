# -*- coding: utf-8 -*-
# setup.py

import ast
import io
import re
from setuptools import setup, find_packages
import sys
import os

# UTF-8 encoding sorunlarını çöz
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def get_version():
    """Parse the AST of __init__.py to find the __version__ assignment safely."""
    with open('grikod2/__init__.py', 'r', encoding='utf-8') as f:
        tree = ast.parse(f.read())
        
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == '__version__':
                    # Eğer atanan değer bir string literal ise (örn: "0.2.9")
                    if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                        return node.value.value
                        
    raise RuntimeError("Unable to find __version__ in grikod2/__init__.py")
"""
def get_version():
    with open('grikod2/__init__.py', 'r', encoding='utf-8') as f:
        content = f.read()
    match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", content, re.M)
    if match:
        return match.group(1)
    raise RuntimeError("Unable to find version string.")
"""

def get_install_requires():
    """Kurulum bağımlılıklarını dinamik olarak belirle"""
    base_requires = [
        "numpy",
    ]

setup(
    name="grikod2",
    version=get_version(),
    description="Binary to Gray code conversion package for efficient data encoding.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Mehmet Keçeci",
    maintainer="Mehmet Keçeci",
    author_email="enfo@tuta.io",
    maintainer_email="enfo@tuta.io",
    url="https://github.com/WhiteSymmetry/grikod2",
    #packages=find_packages(),
    packages=find_packages(
        include=["grikod2", "grikod2.*"],
        exclude=[
            "binder", "content", "data", "notebooks",
            "tests", "tests.*",
            "docs", "docs.*",
            "examples", "examples.*",
            "build", "dist",
            "*.tests", "*.tests.*", ".github",
        ]
    ),
    include_package_data=True,
    package_data={
        "grikod2": ["__init__.py", "_version.py", "*.pyi"]
    },
    install_requires=get_install_requires(),
    extras_require={
        'test': [
            "pytest",
            "pytest-cov",
            "grikod2",
        ],
        'dev': [
            "pytest",
            "pytest-cov",
            "twine",
            "wheel",
            "grikod2",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: AGPL-3.0 License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Mathematics"
    ],
    python_requires='>=3.11',
    license="AGPL-3.0-or-later",
    keywords="grikod2 grikod graycode",
    project_urls={
        "Documentation": "https://github.com/WhiteSymmetry/grikod2",
        "Source": "https://github.com/WhiteSymmetry/grikod2",
        "Tracker": "https://github.com/WhiteSymmetry/grikod2/issues",
    },
)
