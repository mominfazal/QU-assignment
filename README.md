# QU-assignment

## Description

We can run this project the URL : http://35.183.33.171:5000

This project includes 2 APIS:
1) To fetch Twitter tweets as per the handle inserted in the text box. 
2) To fetch the CNN news as per the topic inserted in the text box.

## Code Flow

The APIs are developed using Flask library of Python(It is used to create APIs).
The frontend part is developed using HTML, frontend logic is handled using Jquery and designing is done using Bootstrap.

After hitting the URL, when we click on search button and pass the desired parameter, ajax request to one of the APIs is initiated and JSON response is returned. This response is then converted to HTML and appended to the HTML.

Twitter API works on TWEEPY library which works on TWITTER APIs.
CNN API provides us data which is collected using simple HTTP requests, this requests returns us JSON Data. 


## Installation

To run this project we require below mentioned packages:
Python: (If pip is installed then following commands can help. In case pip is not installed then refer https://www.rosehosting.com/blog/how-to-install-pip-on-ubuntu-16-04 for Ubuntu, https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation for Windows and http://www.pyladies.com/blog/Get-Your-Mac-Ready-for-Python-Programming/ for Mac OS)
1) TWEEPY (pip install tweepy)
2) Flask (pip install flask)
3) Setting flask variable using command :export FLASK_APP=index.py  (Ensure that while hitting you cd into directory of code)

## Run FLASK server
cd /directory-of-code/
python -m flask run

Output must be on URL http://127.0.0.1:5000 for local PCs

## Not working on remote server? 
That is because we need few more things. Just move on with the guide in the URL below step by step and that must do the trick for you. 
https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-14-04

Ensure the PORT you are working on is open.
