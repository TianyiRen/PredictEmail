PredictEmail
============

This is predicting email address project from AlphaSights. In this project, a simple website has been built to 
allow user enter person's first name, last name and domain to predict his/her email address. This project is built
with Django web framework with sqlite3 as backend database. 

## Installation

Prerequists: Python 2.6+ with <a src="https://pip.pypa.io/en/latest/installing.html#install-pip">pip</a> installed<br>
We will use virtual environment to make sure it will not mess up user's environment.<br>
Step 1 install python virtual env:<br>
[sudo]pip install virtualenv<br><br>
Step 2 start virtual environment:<br>
virtualenv ENV<br><br>
Step 3 change to virtual env folder:<br>
cd ENV<br><br>
Step 4 activate virtual environment:<br>
source bin/activate<br><br>
Step 5 git clone:<br>
git clone https://github.com/TianyiRen/PredictEmail.git<br><br>
Step 6 change to project folder:<br>
cd PredictEmail/emailpredict/<br><br>
Step 7 install required package:<br>
[sudo]pip install -r requirements.txt<br><br>
Step 8 synchronize database:<br>
python manage.py syncdb<br><br>
Step 9 migrate database:<br>
python manage.py migrate<br><br>
Step 10 upload dataset provided by AlphaSights:<br>
python manage.py upload_dataset<br><br>
Step 11 runserver:<br>
python manage.py runserver<br><br>
Step 12 access website via browser:<br>
type 127.0.0.1:8000 in browser<br><br>
