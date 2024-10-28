[![Python Package](https://github.com/ptrstn/python-starter/actions/workflows/python-package.yml/badge.svg)](https://github.com/ptrstn/python-starter/actions/workflows/python-package.yml)
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
cp -r tmp/.coveragerc tmp/.flake8 tmp/.gitignore tmp/* .
cp -r tmp/.github .github
rm -rf tmp
```

**Note**: If your project is not empty, it might overwrite your files.

### Adjust package name

Replace all occurrences of ```packagename``` and ```python-starter``` with your package name.

You can do this for instance by first declaring a variable ```NEW_PROJECT_NAME``` and replacing ```<YOUR_PACKAGE_NAME>``` with your desired package/project name.

```bash
NEW_PACKAGE_NAME=<YOUR_PACKAGE_NAME>
```

```bash
NEW_PROJECT_NAME=<YOUR_PACKAGE_NAME>
```

You can then use this variable to rename all occurrences in the template with your desired package/project name.

```bash
mv src/packagename src/$NEW_PACKAGE_NAME
sed -i "s/packagename/$NEW_PACKAGE_NAME/g" pyproject.toml .coveragerc README.md "src/${NEW_PACKAGE_NAME}/__main__.py" tests/test_core.py
sed -i "s/python-starter/$NEW_PROJECT_NAME/g" README.md pyproject.toml
```

### Adjust GitHub Username

If your username is not ```ptrstn``` then you can first setup a new variable:

```bash
YOUR_GH_USERNAME=<YOUR_GITHUB_USERNAME>
```

Then you can replace it with the following command:

```bash
sed -i "s/ptrstn/$YOUR_GH_USERNAME/g" pyproject.toml README.md
```

### Adjust license

Replace the LICENSE file to whatever you want to use. 
I would suggest the MIT license.

### Adjust author 

Also replace the author name in ```pyproject.toml``` with your name.

### Adjust README.md

Adapt README.md, especially the installation instructions, according to your project. 

In particular, delete all the text up until **## Installation**c

```bash
sed -i '6,/## Installation/d' README.md
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
git clone https://github.com/ptrstn/python-starter
cd python-starter
python -m venv venv
. venv/bin/activate
pip install -e .[test]
```

### Testing

```bash
pytest
```
