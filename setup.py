# -*- coding: utf-8 -*-
"""Installer for the imio.webspellchecker package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='imio.webspellchecker',
    version='1.0a1',
    description="An add-on for Plone",
    long_description=long_description,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone',
    author='iMio',
    author_email='antoine.duchene@imio.be',
    url='https://github.com/collective/imio.webspellchecker',
    project_urls={
        'PyPI': 'https://pypi.python.org/pypi/imio.webspellchecker',
        'Source': 'https://github.com/imio/imio.webspellchecker',
        'Tracker': 'https://github.com/imio/imio.webspellchecker/issues'
    },
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['imio'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires="==2.7",
    install_requires=[
        'setuptools',
        'Products.CMFPlone>=4.3.19',
        'Products.GenericSetup>=1.8.2',
        'plone.api'
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.testing>=5.0.0'
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = imio.webspellchecker.locales.update:update_locale
    """,
)
