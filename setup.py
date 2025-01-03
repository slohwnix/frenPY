from setuptools import find_packages, setup

setup(
    name='frenpy',
    packages=find_packages(include=['frenpy']),
    version='0.3.6',
    description='French python',
    author='slohwnix',
    install_requires=[],
    package_data={
        'frenpy': ['words.json'],
    },
    include_package_data=True,
)
