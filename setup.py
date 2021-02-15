
#!/usr/bin/env python
'''
Installer script for sowsbetter.
'''

from setuptools import setup

import re
VERSIONFILE="_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

setup(
    name = "sowsbetter",
    description = "Automatically transcode and upload FLACs on bemaniso.ws.",
    version = verstr,
    url = 'https://dev.s-ul.eu/Doggo404/sowsbetter/',
    py_modules = [
        '_version',
        'tagging',
        'transcode',
        'whatapi'
    ],
    scripts = ['sowsbetter'],
    install_requires = [
        'mutagen>=1.20',
        'mechanize==0.2.5',
        'requests>=1.0'
    ]
)
