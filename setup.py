import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='drf-ip-restrictions',
    version=os.getenv('PACKAGE_VERSION', '0.0.0').replace('refs/tags/', ''),
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A library that allows IP restrictions for views/endpoints in Django REST framework.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/anexia/drf-ip-restrictions',
    author='Alexandra Bruckner',
    author_email='abruckner@anexia-it.com',
    install_requires=[
        'django>=4.2',
        'djangorestframework>=3.15',
        'django-ipware>=4.0.2',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Framework :: Django :: 4.2',
        'Framework :: Django :: 5.0',
        'Framework :: Django :: 5.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
)
