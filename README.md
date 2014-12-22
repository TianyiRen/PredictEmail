PredictEmail
============

This is predicting email address project from AlphaSights. In this project, a simple website has been built to 
allow user enter person's first name, last name and domain to predict his/her email address. This project is built
with Django web framework with sqlite3 as backend database. 

## Installation

Prerequists: Python 2.6+ with <a src="https://pip.pypa.io/en/latest/installing.html#install-pip">pip</a> installed
We will use virtual environment to make sure it will not mess up user's environment.
Step 1 install python virtual env:
[sudo]pip install virtualenv
Step 2 start virtual environment:
virtualenv ENV
Step 3 change to virtual env folder:
cd ENV
Step 4 activate virtual environment:
source bin/activate
Step 5 git clone:
git clone https://github.com/TianyiRen/PredictEmail.git
Step 6 change to project folder:
cd PredictEmail/emailpredict/
Step 7 install required package:
[sudo]pip install -r requirements.txt
Step 8 synchronize database:
python manage.py syncdb
Step 9 migrate database:
python manage.py migrate
Step 10 upload dataset provided by AlphaSights:
python manage.py upload_dataset
Step 11 runserver:
python manage.py runserver
Step 12 access website via browser:
type 127.0.0.1:8000 in browser
