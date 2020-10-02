#!/usr/bin/env python

import setuptools

setuptools.setup(
    # basic
    name='nlp-sandbox-evaluation',
    version='0.1.0',
    # packages=setuptools.find_packages(exclude=["tests", "tests.*"]),
    # py_modules=['hello'],
    # scripts=['bin/nlp-evaluate'],

    packages=[
        'cli',
        'evaluate'
    ],
    entry_points={
        'console_scripts': ['nlp-cli=cli.__main__:cli']
    },

    # requirements
    python_requires='>=3.6.*',
    install_requires=[
        'click>=7.1.2',
        'jsonschema>=3.2.0'
    ],

    # metadata to display on PyPI
    description='Evaluate the performance of NLP Sandbox Tools',
    long_description="TBA",
    long_description_content_type="text/markdown",
    url='https://www.synapse.org/nlp_sandbox',
    author='The NLP Sandbox Team',
    author_email='thomas.schaffter@sagebionetworks.org',
    license='Apache',
    project_urls={
        "Source Code": "https://github.com/data2health/nlp-sandbox-evaluation",
        "Bug Tracker": "https://github.com/data2health/nlp-sandbox-evaluation/issues",
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