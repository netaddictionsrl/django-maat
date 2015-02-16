from setuptools import setup, find_packages

APP_NAME = 'djangomaat'

setup(
    name=APP_NAME,
    version=".".join(map(str, __import__(APP_NAME).VERSION)),
    packages=find_packages(),
    include_package_data=True,
    description = 'Fast MySQL ordering',
    author = 'Germano Guerrini',
    author_email = 'germano.guerrini@gmail.com',
    url = 'https://github.com/GermanoGuerrini/django-maat',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
)
