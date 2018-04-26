from setuptools import setup, find_packages

setup(
    name='log_cleaner',
    version='1.0.1',
    description='clean outdated log.',
    packages=find_packages(),
    author='lisfe',
    author_email='lisfegm@gmail.com',
    install_requires=[],
    entry_points = {
        'console_scripts':[
            'log-clean = log_cleaner.main:main',
        ]
    }
)
