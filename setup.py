#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os
import re
import sys

try:
    import pypandoc
    readme = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    readme = ''


package = 'tapioca_sectigo_api_ssl'
requirements = [
    'tapioca-wrapper<2',

]
test_requirements = [

]


def get_author(package):
    """
    Return package author as listed in `__author__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("^__author__ = ['\"]([^'\"]+)['\"]",
                     init_py, re.MULTILINE).group(1)


def get_email(package):
    """
    Return package email as listed in `__email__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("^__email__ = ['\"]([^'\"]+)['\"]",
                     init_py, re.MULTILINE).group(1)


# python setup.py register
if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    print("You probably want to also tag the version now:")
    print("  git tag -a %(version)s -m 'version %(version)s'" % args)
    print("  git push --tags")
    sys.exit()


setup(
    name='tapioca-sectigo_api_ssl',
    version_format='{tag}.dev{commitcount}',
    setup_requires=['setuptools-git-version'],
    description='sectigo_api_ssl API wrapper using tapioca',
    long_description=readme,
    author=get_author(package),
    author_email=get_email(package),
    url='https://github.com/Smogin/tapioca-sectigo_api_ssl',
    packages=[
        'tapioca_sectigo_api_ssl',
    ],
    package_dir={'tapioca_sectigo_api_ssl': 'tapioca_sectigo_api_ssl'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='sectigo_api_ssl',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)

