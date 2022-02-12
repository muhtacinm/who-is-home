# who-is-home

## About

This app is used to detect if each cars specified are at the home residency. It utilizes Wyze Cameras RTSP feed and grabs an image from the live feed. 
It then grabs each car expected position from the image then uses OPENCV to detect if a car object exists. 

## Features

1. Informs user on who is home depending on car location. 



## Pages

### Landing Page

![alt text](https://github.com/muhtacinm/who-is-home/blob/master/examples/landing.png?raw=true)

### Car 1 (Not Home)

![alt text](https://github.com/muhtacinm/who-is-home/blob/master/examples/car1.png?raw=true)


### Car 2 (Home)

![alt text](https://github.com/muhtacinm/who-is-home/blob/master/examples/car2.png?raw=true)


### Car 3 (Home)

![alt text](https://github.com/muhtacinm/who-is-home/blob/master/examples/car3.png?raw=true)

## Running Locally

Make sure you have Python installed

After clone

```
$ git clone https://github.com/muhtacinm/who-is-home.git # or clone your own fork
$ cd who-is-home
$ pip install -r requirements.txt
$ python app.py
```

App should now be running on [localhost:5000](http://localhost:5000/).

## Wyze Camera RTSP Faq/Setup 

https://support.wyze.com/hc/en-us/articles/360026245231-Wyze-Cam-RTSP
