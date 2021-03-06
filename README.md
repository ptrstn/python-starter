[![Actions Status](https://github.com/ptrstn/python-starter/workflows/Python%20package/badge.svg)](https://github.com/ptrstn/python-starter/actions)
[![Build Status](https://travis-ci.com/ptrstn/python-starter.svg?branch=master)](https://travis-ci.com/ptrstn/python-starter)
[![codecov](https://codecov.io/gh/ptrstn/python-starter/branch/master/graph/badge.svg)](https://codecov.io/gh/ptrstn/python-starter)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# python-starter

My personal python starter template. Intended for copy and paste use. 

This project is released into the public domain, so feel free to modify and use it as you wish.

## Usage

### Copy files into your new project

Copy all files from this repository into your personal project. 

```bash
git clone https://github.com/ptrstn/python-starter.git tmp
rm -rf tmp/.git
cp -r tmp/.coveragerc tmp/.gitignore tmp/.travis.yml tmp/* .
rm -rf tmp
```

**Note**: If your project is not empty, it might overwrite your files.

### Adjust package name

Replace all occurrences of ```packagename``` with your package name.

```bash
NEW_PROJECT_NAME=<YOUR_PACKAGE_NAME>
mv packagename $NEW_PROJECT_NAME
sed -i "s/packagename/$NEW_PROJECT_NAME/g" setup.py .coveragerc "${NEW_PROJECT_NAME}/__main__.py" tests/test_core.py .travis.yml
```

### Adjust license

Replace the LICENSE file and change the ```license=Unlicense``` entry in ```setup.py``` to whatever you want to use. 
I would suggest the MIT license.

### Adjust author 

Also replace the author name in ```setup.py``` with your name.

### Adjust README.md

Adapt README.md, especially the installation instructions, according to your project. 

In particular, change the following entries:

- GitHub url
- Travis CI badge url
- codecov badge url

## Installation

```bash
pip install --user git+https://github.com/ptrstn/python-starter
```

## Usage

```bash
packagename
```

## Development

```bash
git clone https://github.com/ptrstn/python-starter
cd python-starter
pip install -e .
pip install -r testing-requirements.txt
```

### Testing

```bash
pytest
```
