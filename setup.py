import setuptools
from setuptools import setup
from sso import __version__


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pod-sso",
    version=__version__,
    url="https://github.com/FanapSoft/pod-sso-python-sdk",
    license="MIT",
    author="ReZa ZaRe",
    author_email="rz.zare@gmail.com",
    description="This package for implementation of POD platform SSO APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["pod", "single sign on", "sso", "pod sdk"],
    packages=setuptools.find_packages(exclude=("build", "dist")),
    install_requires=[
        "pod-base>=1,<2",
        "pycrypto>=2.6.1"
    ],
    classifiers=[
        "Natural Language :: English",
        "Natural Language :: Persian",
    ],
    python_requires='>=2.7',
    package_data={
        'sso': ['*.ini', '*.json']
    },
    project_urls={
        "Documentation": "http://docs.pod.ir/v1.0.0.2/PODSDKs/python/5233/user",
        "Source": "https://github.com/FanapSoft/pod-sso-python-sdk",
        "Tracker": "https://github.com/FanapSoft/pod-sso-python-sdk/issues"
    }
)
