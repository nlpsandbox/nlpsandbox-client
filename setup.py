#!/usr/bin/env python

import setuptools

setuptools.setup(
    # basic
    name='nlp-sandbox-client',
    version='0.1.1',
    # packages=setuptools.find_packages(exclude=["tests", "tests.*"]),
    # py_modules=['hello'],
    # scripts=['bin/nlp-evaluate'],

    packages=[
        'nlpsandboxclient'
    ],
    entry_points={
        'console_scripts': ['nlp-cli=nlpsandboxclient.__main__:main']
    },

    # requirements
    python_requires='>=3.6.*',
    install_requires=[
        'click>=7.1.2',
        'jsonschema>=3.2.0',
        'synapseclient>=2.2.0'
    ],

    # metadata to display on PyPI
    description='Python client for the NLP Sandbox',
    long_description="TBA",
    long_description_content_type="text/markdown",
    url='https://www.synapse.org/nlp_sandbox',
    author='The NLP Sandbox Team',
    author_email='thomas.schaffter@sagebionetworks.org',
    license='Apache',
    project_urls={
        "Source Code": "https://github.com/Sage-Bionetworks/nlp-sandbox-client",
        "Bug Tracker": "https://github.com/Sage-Bionetworks/nlp-sandbox-client/issues",
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics'
    ]
)
