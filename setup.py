#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = "pySOFA",
    version = "0.0.1",
    author = r"Jörg Encke",
    author_email = "joerg.encke@tum.de",

    description = "SOFA API",
    license = "GPLv3+",
    url = "https://github.com/mrkrd/thorns",
    download_url = "https://github.com/mrkrd/thorns/tarball/master",

    platforms = ["Linux", "Windows"],
    install_requires=["pytables"],
)
