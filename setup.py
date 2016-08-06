try:
    from setuptools import setup
except ImportError:
    from distutils.code import setup

setup(
    name='waage',
    description='',
    packages=['waage'],
    install_requires=[
        'Django',
    ],
    entry_points={
        'console_scripts': ['waage=waage.commandline:main'],
    },
)
