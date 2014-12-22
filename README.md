PredictEmail
============

This is predicting email address project from AlphaSights. In this project, a simple website has been built to allow user enter person's first name, last name and domain to predict his/her email address. This project is built with Django web framework with sqlite3 as backend database. 

## Installation

Prerequists: Python 2.6+ with [pip](https://pip.pypa.io/en/latest/installing.html#install-pip) installed<br>
We will use virtual environment to make sure it will not mess up user's environment.<br>
1. install python virtual env:<br>
	_[sudo]pip install virtualenv_<br><br>
2. start virtual environment:<br>
	_virtualenv ENV_<br><br>
3. change to virtual env folder:<br>
	_cd ENV_<br><br>
4. activate virtual environment:<br>
	_source bin/activate_<br><br>
5. git clone:<br>
	_git clone https://github.com/TianyiRen/PredictEmail.git_<br><br>
6. change to project folder:<br>
	_cd PredictEmail/emailpredict/_<br><br>
7. install required package:<br>
	_[sudo]pip install -r requirements.txt_<br><br>
8. Clear database:<br>
	_python manage.py flush_<br><br>
9. synchronize database:<br>
	_python manage.py syncdb_<br><br>
10. migrate database:<br>
	_python manage.py migrate_<br><br>
11. upload dataset provided by AlphaSights:<br>
	_python manage.py uploaddataset_<br><br>
12. runserver:<br>
	_python manage.py runserver_<br><br>
13. access website via browser:<br>
	_type 127.0.0.1:8000 in browser_<br><br>
