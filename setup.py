from setuptools import setup

import blog

setup(
    name="django-blog",
    version=blog.__version__,
    description="Reusable, generic blog for Django",
    long_description="A basic 'blog' app perfect for website announcements / basic blog page.",
    keywords="django, views, forms, mixins",
    author="James Tarball <james.tarball@gmail.com>",
    author_email="james.tarball@gmail.com",
    url="https://github.com/JTarball/django-blog",
    license="BSD",
    packages=["django-blog"],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: BSD License",
        "Environment :: Web Environment",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Framework :: Django",
        "Framework :: Django :: 1.8",
    ],
)
