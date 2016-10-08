from setuptools import setup

import django_blog

setup(
    name="django-blog",
    version="0.1.0",
    description="Resuable, generic blog app for Django",
    long_description="A basic 'blog' app perfect for website announcements / basic blog page",
    keywords="django",
    author="James Tarball <james.tarball@gmail.com>",
    author_email="james.tarball@gmail.com",
    url="https://github.com/JTarball/django-blog",
    license="Not open source",
    packages=["django_blog"],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Web Environment",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Framework :: Django",
        "Framework :: Django :: 1.8",
    ],
)
