PredictEmail
============

This is predicting email address project from AlphaSights. In this project, a simple website has been built for users to enter person's first name, last name and domain to predict his/her email address. This project is built with Django web framework with sqlite3 as backend database. 

## Installation

Prerequists: Python 2.6+ with [pip](https://pip.pypa.io/en/latest/installing.html#install-pip) installed<br>
We will use virtual environment to make sure it will not mess up user's environment.<br>
1. install python virtual env:<br>
	$ [sudo]pip install virtualenv<br><br>
2. start virtual environment:<br>
	$ virtualenv ENV<br><br>
3. change to virtual env folder:<br>
	$ cd ENV<br><br>
4. activate virtual environment:<br>
	$ source bin/activate<br><br>
5. git clone:<br>
	$ git clone https://github.com/TianyiRen/PredictEmail.git<br><br>
6. change to project folder:<br>
	$ cd PredictEmail/emailpredict/<br><br>
7. install required package:<br>
	$ [sudo]pip install -r requirements.txt<br><br>
8. synchronize database:<br>
	$ python manage.py syncdb<br><br>
9. migrate database:<br>
	$ python manage.py migrate<br><br>
10. upload dataset provided by AlphaSights:<br>
	$ python manage.py uploaddataset<br><br>
11. runserver:<br>
	$ python manage.py runserver<br><br>
12. access website via browser:<br>
	_type 127.0.0.1:8000 in browser (suggest to run in Chrome)_<br><br>

## Basic Idea
To predict email address, one needs to provide first name, last name and domain. Possible email address is predicted according to the probablities of possible patterns used by a company (domain). If a company is using different patterns, it will return all possible email patterns with corresponding probabilities (stored in the database). If we cannot verify which pattern to use, we store all possible predicted emails into the database; if we can verify one of them, we just store the verified one into the database and discard the rest. 
