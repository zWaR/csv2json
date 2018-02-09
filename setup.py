
from setuptools import setup

setup(
    name="csv2json",
    version="1.0.0",
    description="A tool for csv to json file conversion",
    author="zWaR",
    author_email="zwar@sharklasers.com",
    classifiers=[
        "Indetend Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6"
    ],
    keywords="csv json conversion tool",
    packages=["src"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov", "pyfakefs", "pytest-mypy"],
    url="https://github.com/zWaR/csv2json",
    project_urls={
        "Source Code": "https://github.com/zWaR/csv2json.git",
        "Bug Tracker": "https://github.com/zWaR/csv2json/issues",
        "Documentation": "https://github.com/zWaR/csv2json"
    },
    entry_points={
        "console_scripts": [
            "csv2json = src.main:main"
        ]
    }
)
