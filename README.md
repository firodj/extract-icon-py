extract-icon-py
===============

Extract Icon from PE Executable with Python.

Requirements
------------

```
$ pip install -r requirements.txt
```

Testing
-------

Install pytest first:

```
pip install -U pytest
```

Then run tests:

```
$ py.test
```

References
----------
* [CodeProject - Get icons from Exe or DLL the PE way](http://www.codeproject.com/Articles/9303/Get-icons-from-Exe-or-DLL-the-PE-way)

Pyhon 2.7
---------

```
$ pyenv local 2.7.18
$ python -m virtualenv venv27
$ source venv27/bin/activate
$ pip install -r requirements-27.txt
...
$ deactivate
```

Python 3.11
-----------

```
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
