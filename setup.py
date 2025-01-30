from os import path
from setuptools import setup, find_packages

with open(path.join(path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

setup(
    name="starkbank-iso8583",
    packages=find_packages(),
    include_package_data=True,
    description="Python library for conversion between ISO 8583 message standard and JSON",
    long_description=README,
    license="MIT License",
    url="https://github.com/starkbank/iso8583-python",
    author="Stark Bank",
    author_email="developers@starkbank.com",
    keywords=["iso8583", "credit card", "debit card", "mastercard", "visa"],
    version="0.6.0"
)

"""
Deployment instructions
-----------------------

Global
~~~~~~

Before deployment, change the project *version* on ``setup.py`` file and
set the correct *download*\ url\_. Then make sure you have the file
``~/.pypirc`` with the content below and the correct credentials instead
of the provided placeholders:

::

    [distutils]
    index-servers =
        pypi
        pypitest

    [pypi]
    repository:https://upload.pypi.org/legacy/
    username:myusername
    password:mypassword

    [pypitest]
    repository:https://test.pypi.org/legacy/
    username:myusername
    password:mypassword

### Create a source distribution:

Run ```python setup.py sdist``` inside the project directory.

### Install twine:

```pip install twine```

### Upload package to pypi:

```twine upload dist/*```


Live environment
~~~~~~~~~~~~~~~~

For unit test:

```
python -m unittest discover -s febraban/cnab240/tests -p '*Test.py'
```

To release a new version:

```
python setup.py sdist upload -r pypi`` inside the project
```

"""