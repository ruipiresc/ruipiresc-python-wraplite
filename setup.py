import os
import sys
from setuptools import setup

def publish(option: str = 'build') -> None:
    os.system('python -m bumpversion ' + option)
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()

if sys.argv[-1] == 'publish':
    if sys.argv[-2] == 'patch':
        publish('patch')
    elif sys.argv[-2] == 'minor':
        publish('minor')
    elif sys.argv[-2] == 'major':
        publish('major')
    elif sys.argv[-2] == 'build':
        publish('build')
    elif sys.argv[-2] == 'release':
        publish('--tag release')

about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'wraplite', '__version__.py')) as f:
    exec(f.read(), about)

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name=about['__title__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=['wraplite'],
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=['pandas'],
    license=about['__license__'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy'
        'Programming Language :: SQL',
        'Topic :: Utilities'
    ],
    keywords='nosql sqlite wrapper wraplite sql'
)