#!/usr/bin/env python

from setuptools import setup, find_packages
from sos import __version__ as VERSION


setup(
    name='doca-sosreport',
    version=VERSION,
    # to avoid a packaging dependency on older RHELs
    # we only declare it on recent Python versions
    install_requires=['pexpect', 'pyyaml', 'packaging;python_version>="3.11"'],
    description=(
        'A set of tools to gather troubleshooting information from a system'
    ),
    author='Bryn M. Reeves',
    author_email='bmr@redhat.com',
    maintainer='Jake Hunsaker',
    maintainer_email='jacob.r.hunsaker@gmail.com',
    url='https://github.com/sosreport/sos',
    license="GPLv2+",
    scripts=['bin/sos'],
    data_files=[
        ('share/man/man1', ['man/en/sos-report.1', 'man/en/sos.1',
                            'man/en/sos-collect.1', 'man/en/sos-clean.1',
                            'man/en/sos-mask.1', 'man/en/sos-help.1',
                            'man/en/sos-upload.1']),
        ('share/man/man5', ['man/en/sos.conf.5']),
        ('share/licenses/doca-sosreport', ['LICENSE']),
        ('share/doc/doca-sosreport', ['AUTHORS', 'README.md']),
        ('config', ['sos.conf', 'sos-mlx-cloud-verification.conf',
                    'sos-nvidia.conf', 'sos-nvdebug.conf',
                    'tmpfiles/tmpfilesd-sos-rh.conf'])
    ],
    packages=find_packages(include=['sos', 'sos.*'])
)

# vim: set et ts=4 sw=4 :
