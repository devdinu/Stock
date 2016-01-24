# Stocks - A Python Environment

[![Build Status](https://travis-ci.org/dineshkumar-cse/Stock.svg?branch=master)](https://travis-ci.org/dineshkumar-cse/Stock)

### A Sample Project to describe, or uses the pyton environment extensively

* pyenv virtualenvironment
* Ansible provisioning / setup
* Unit Tests
* Travis Ci Integration

### Install Dependencies

* preferred to have run `./local_build.sh` but to be precise, run `pip intall -r requirements.txt`, requirements.txt contains the dependencies for the project.

### Run Application

* To Run the App `python stock_market.py`, uses `app.run(*args)` and start the service
* losers and gainers endpoint also supports json, request json by passing query parameter `json=t or json=true`
    - eg: http://localhost:5000/losers?json=t

### Run Ansible Script

```
ansible-playbook -i 'vagrant@ip', setup.yml # Running for remote/vagrant maching 
ansible-playbook -i 'localhost', setup.yml -c local # Running for remote/vagrant maching #To Run locally
```

### Run Unit Tests

```python -m unittest discover tests . "*_test.py" 
```
pattern not required if you have tests with convention test_*.py

### To Break localbuild if any of linter/ jobs fails
Add this to the localbuild.sh file
```#!/bin/bash -e
```

or `set -e` in terminal. This exits the script if any command returns non-zero value or FAILS (echo $?).


### Summary

This project mostly uses, exposes you to the following,


* Need For Environment?
    - conflicts across libraries || python versions
    - print "" fails in python3+
    - generator.next() fails in python3+
* pyenv
    - `pyenv versions` lists all python versions available (2.7, 3.2, 3.4.1 ...)
    - `pyenv shell` - to activate a specific python version (PYENV_VERSION)
* pyenv virtualenv
  - install python version (`pyenv install 2.7`)
  - install virtualenvironment (`pyenv virtualenv 2.7 stock_env`)
  - `pyenv activate` to activate virtualenv or put virtualenv name in `.python-version` file
* pip manages the dependency modules
    - `pip list` show all modules
    - `pip freeze > requirements.txt` to update requirements file. 
* Tests... Unit Tests... TDD! Try to Have more Tests/Test Coverage. No Documentation :) 
* linters
    - pep8, pyflakes, **pylint**
* basic service with flask
* ansible to setup projects
* __file__, __name__, __main__ ...
* PYTHONVERBOSE, PYTHONPATH 
    - `export PYTHONVERBOSE="bla"` to have more debugging info
    - `unset PYTHONVERBOSE` to remove debugging info


Reference:
* [pyenv-virtualenv](https://github.com/yyuu/pyenv-virtualenv)
* [python unittest](https://docs.python.org/2/library/unittest.html)
* [setup travis ci for python](https://docs.travis-ci.com/user/languages/python)
