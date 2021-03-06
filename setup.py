"""
Exif.py
written by Gene Cash for reading EXIF and IPTC data in python.
Original repo has gone offline so i'm making it public here for my personal projects.
"""

from distutils.core import setup


VERSION = '0.1.0'

setup(
    name='exif',
    version=VERSION,
    author='genecash',
    description='for reading EXIF and IPTC data',
    platforms=['any'],
    url='http://github.com/gregnewman/exif',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        ],
    packages=[
        'exif',
        ],
    )
