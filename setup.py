from setuptools import setup, find_packages


setup(
    name='planet_rest_api',
    version='1.0.0',
    description='REST API coding challenge for Planet Labs',
    long_description=open('README.rst').read(),
    keywords=[
        
    ],
    author='Todd Wolfson',
    author_email='todd@twolfson.com',
    url='https://github.com/twolfson/planet-rest-api',
    download_url='https://github.com/twolfson/planet-rest-api/archive/master.zip',
    packages=find_packages(),
    license='UNLICENSE',
    install_requires=open('requirements.txt').readlines(),
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
