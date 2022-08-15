#!/usr/bin/env python3

from setuptools import find_packages
from setuptools import setup

setup(
    name='wazo-confd-power_dialer',
    version='0.1',
    description='Connectino power_dialer plugin',
    author='Farhad K',
    author_email='foo@bar.com',
    packages=find_packages(),
    url='https://www.foo-bar.com',
    include_package_data=True,
    package_data={
        'wazo_confd_power_dialer': ['api.yml'],
    },
    entry_points={
        'wazo_confd.plugins': [
            'power_dialer = wazo_confd_power_dialer.plugin:Plugin'
        ]
    }
)
