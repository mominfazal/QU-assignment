# QU-assignment

## Description

We can run this project the URL : 172.31.18.197

This project includes 2 APIS:
1) To fetch Twitter tweets as per the handle inserted in the text box. 
2) To fetch the CNN news as per the topic inserted in the text box.

## Code Flow

The APIs are developed using Flask library of Python(It is used to create APIs).
The frontend part is developed using HTML, frontend logic is handled using Jquery and designing is done using Bootstrap.

When we click on search button, ajax request to one of the APIs is initiated and JSON response is returned. This response is then converted to HTML and appended to the HTML.

Twitter API works on TWEEPY library which works on TWITTER APIs.
CNN API provides us data which is collected using simple HTTP requests, this requests returns us JSON Data. 


## Installation

To run this project we require below mentioned packaged:
Python:
1) TWEEPY
2) Flask
