# Coding Dojo

## Setup

1. Install [pyenv](https://github.com/pyenv/pyenv#getting-pyenv)
2. Install python `3.8.10`
3. Install [poetry](https://python-poetry.org/docs/#installation)
4. Git clone project
5. Run `pyenv local 3.8.10`
6. Create and activate python shell with `poetry env use $PYENV_ROOT/shims/python3.`
7. Run `poetry install`

## Run Tests

Run `pytest tests`
