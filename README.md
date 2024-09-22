# Python + behave example

This repository contains the code for an example using Behave and Python.
The E2E tests are written using [Behave](https://behave.readthedocs.io/en/stable/) and run
using [Selenium](https://www.selenium.dev/).
The API tests are written using [Pytest](https://docs.pytest.org/en/stable/)
and [Requests](https://docs.python-requests.org/en/latest/).

E2E tests are located in the `features` folder and API tests are located in the `tests` folder.

## Requirements

- Python 3.11
- Pipenv

## Installation

After cloning the repository, run the following command to install the dependencies:

```bash
pipenv install
```

## Running

To run the E2E tests, run the following command:

```bash
pipenv run behave
```

To run the API tests, run the following command:

```bash
pipenv run pytest
```
