from setuptools import setup, find_packages

__author__ = "Manuel Huber"
__version__ = "0.0.1"

setup(
    name='dummy-mod',
    version=__version__,
    description='Dummy module with a simple cli program',
    author=__author__,
    classifiers=[
        "Programming Language :: Python :: 3 :: Only"
    ],
    package_dir={
        '': 'src'
    },
    packages=find_packages(where='./src'),
    package_data={
        'dummy_mod': ['data/dummy-file.txt']
    },
    entry_points={
        'console_scripts': [
            'dummy-cli = dummy_mod:main',
        ]
    }
)
