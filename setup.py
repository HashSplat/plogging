"""
    setup.py - Setup file to distribute the library
See Also:
    https://github.com/pypa/sampleproject
    https://packaging.python.org/en/latest/distributing.html
    https://pythonhosted.org/an_example_pypi_project/setuptools.html
"""
import os
import glob

from setuptools import setup


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


def read(fname):
    """Read in a file"""
    with open(os.path.join(os.path.dirname(__file__), fname), "r") as file:
        return file.read()


if __name__ == "__main__":
    # ===== Requirements =====
    try:
        requirements = parse_requirements("requirements.txt")
    except FileNotFoundError:
        requirements = []
    # ===== END Requirements =====

    setup(
        name="plogging",
        version="1.0.4",
        description="Log data quickly with a separate process.",
        url="https://github.com/justengel/plogging",
        download_url="https://github.com/justengel/plogging/archive/v1.0.4.tar.gz",

        keywords=["logging", "plogging", "process", "process logging", "parallel logging"],

        author="Justin Engel",
        author_email="jtengel08@gmail.com",

        license="MIT",

        platforms="any",
        classifiers=["Programming Language :: Python",
                     "Programming Language :: Python :: 3",
                     "Operating System :: OS Independent"],

        scripts=[],

        long_description=read("README.md"),
        packages=["plogging"],
        install_requires=requirements,

        include_package_data=False,

        # package_data={
        #     'package': ['file.dat']
        # }

        # options to install extra requirements
        # extras_require={
        #     'dev': [],
        #     'test': ['converage'],
        # }

        # Data files outside of packages
        # data_files=[('my_data', ["data/my_data.dat"])],

        # keywords='sample setuptools development'

        # entry_points={
        #     'console_scripts': [
        #         'foo = my_package.some_module:main_func',
        #         'bar = other_module:some_func',
        #     ],
        #     'gui_scripts': [
        #         'baz = my_package_gui:start_func',
        #     ]
        # }
    )
