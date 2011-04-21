#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='GLAMkit Static-Preload',
    version='0.1',
    description='An app allowing views to be served statically in Django.',
    author='The Interaction Consortium',
    author_email='admins@interaction.net.au',
    #url='http://',
    packages=['static_preload',],
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)
