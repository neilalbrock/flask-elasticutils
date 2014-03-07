import os

from setuptools import setup


def _read(fn):
    path = os.path.join(os.path.dirname(__file__), fn)
    return open(path).read()

setup(
    name='Flask-ElasticUtils',
    version='0.1.1',
    url='https://github.com/neilalbrock/flask-elasticutils/',
    license='BSD',
    author='Neil Albrock - Atomised',
    author_email='neil@atomised.coop',
    description='ElasticUtils for Flask',
    long_description=_read('README.rst'),
    py_modules=['flask_elasticutils'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'elasticutils>=0.9.dev',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
