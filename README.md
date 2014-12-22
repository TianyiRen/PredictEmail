PredictEmail
============

This is predicting email address project from AlphaSights. In this project, a simple website has been built to allow user enter person's first name, last name and domain to predict his/her email address. This project is built with Django web framework with sqlite3 as backend database. 

## Installation

Prerequists: Python 2.6+ with [pip](https://pip.pypa.io/en/latest/installing.html#install-pip) installed<br>
We will use virtual environment to make sure it will not mess up user's environment.<br>
1. install python virtual env:
	_[sudo]pip install virtualenv_
2. start virtual environment:
	_virtualenv ENV_
3. change to virtual env folder:
	_cd ENV_
4. activate virtual environment:
	_source bin/activate_
5. git clone:
	_git clone https://github.com/TianyiRen/PredictEmail.git_
6. change to project folder:
	_cd PredictEmail/emailpredict/_
7. install required package:
	_[sudo]pip install -r requirements.txt_
8. synchronize database:
	_python manage.py syncdb_
9. migrate database:
	_python manage.py migrate_
10. upload dataset provided by AlphaSights:
	_python manage.py uploaddataset_
11. runserver:
	_python manage.py runserver_
12. access website via browser:
	_type 127.0.0.1:8000 in browser_
