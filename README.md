# who-is-home

## About

This app is used to detect if each cars specified are at the home residency. It utilizes Wyze Cameras RTSP feed and grabs an image from the live feed. 
It then grabs each car expected position from the image then uses OPENCV to detect if a car object exists. 

## Features

1. Informs user on who is home depending on car location. 


## Running Locally

Make sure you have Python installed

After clone

```
$ pip install -r requirements.txt
$ python app.py
```

App should now be running on [localhost:5000](http://localhost:5000/).

## WYZE RTSP FAQ/SETUP 

https://support.wyze.com/hc/en-us/articles/360026245231-Wyze-Cam-RTSP