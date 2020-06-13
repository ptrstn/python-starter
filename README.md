[![Build Status](https://travis-ci.com/ptrstn/python-starter.svg?branch=master)](https://travis-ci.com/ptrstn/python-starter)
[![codecov](https://codecov.io/gh/ptrstn/python-starter/branch/master/graph/badge.svg)](https://codecov.io/gh/ptrstn/python-starter)

# python-starter

My personal python starter template. Intended for copy and paste use. 

This project is released into the public domain, so feel free to modify and use it as you wish.

## How to use

### Adjust package name

Copy these files into your personal project and replace all occurrences of ```packagename``` with your package name.

```bash
mv packagename <YOUR-PACKAGENAME>
```

### Adjust license

Replace the license to whatever you want to use. Replace the LICENSE file and change the ```license=Unlicense``` entry in ```setup.py```

### Adjust setup.py

Also change the author name in ```setup.py``` to your name.

```python
setup(
    name="<YOUR-PACKAGE-NAME>",
    version=find_version("<YOUR-PACKAGE-NAME>", "__init__.py"),
    url="http://github.com/<YOUR-GITHUB-ACCOUNT>/<YOUR-GITHUB-PROJECT>",
    author="<YOUR NAME>",
    license="<YOUR LICENSE>",
    packages=["<YOUR-PACKAGE-NAME>"],
    install_requires=[],
    entry_points={"console_scripts": ["<YOUR-PACKAGENAME>=<YOUR-PACKAGENAME>.__main__:main"]},
)
```

### Adjust README.md

Adapt the README.md, especially the installation instructions, according to your project. 

In particular, change the following entries:

- GitHub url
- Travis CI badge url
- codecov url

### Test changes

Follow the development instructions and run the tests to ensure that everything is running properly.

```bash
pip install -e .
pip install -r testing-requirements.txt
pytest
```

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
git clone https://github.com/ptrstn/packagename
cd packagename
pip install -e .
pip install -r testing-requirements.txt
```

### Testing

```bash
pytest
```
