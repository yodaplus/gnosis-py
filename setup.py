import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

requirements = [
    "cached-property>=1.5; python_version < '3.8'",
    "ethereum>=2.3.2",
    "packaging",
    "py-eth-sig-utils>=0.3.0",
    "typing-extensions==3.10.0.0; python_version < '3.8'",
    "requests>=2",
    "web3>=5.18,<=5.19",
]

extras_require = {
    "django": ["django>=2", "django-filter>=2", "djangorestframework>=2"]
}

setup(
    name='yodaplus-py',
    version='0.9.1',
    packages=find_packages(),
    package_data={'gnosis': ['py.typed']},
    install_requires=requirements,
    include_package_data=True,
    extras_require=extras_require,
    python_requires='>=3.7',
    license='MIT License',
    description='Yodaplus libraries for Python Projects',
    long_description=README,
    url='https://github.com/yodaplus/gnosis-py',
    author='Yodaplus',
    author_email='hello@yodaplus.com',
    keywords=['xdc', 'django', 'rest', 'yplusvault'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
