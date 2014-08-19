# -*- coding: utf-8 -*-

from setuptools import setup
from pip.req import parse_requirements

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements('requirements/prod.txt')

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]

project = 'biomics'

setup(
    name=project,
    version='0.1',
    url='https://github.com/eurushibata/biomics-api',
    description='biOMiCs API',
    author='Emerson Urushibata',
    author_email='urushibata.emerson@gmail.com',
    packages=["biomics"],
    include_package_data=True,
    zip_safe=False,
    install_requires=reqs,
    test_suite='tests',
    classifiers=[
    ]
)