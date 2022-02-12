#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect, url_for
from modules.wyzeImage import * 

DEVELOPMENT_ENV  = True

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

app_data = {
    "name":         "Check Who is Home?",
    "description":  "A basic Flask app using bootstrap for layout",
    "author":       "Muhtacin Manik",
    "html_title":   "Check Who is Home?",
    "project_name": "Who Is Home?",
}


## possible values
names=["car1", "car2", "car3"]

@app.route('/')
def index():
    #saveLiveImage()
    return render_template('index.html', app_data=app_data, names=names)

@app.route('/tem')
def tem():
    #saveLiveImage()
    return render_template('tem.html')



@app.route('/who/<name>')
def who(name):
    saveLiveImage()
    if name in names:
        if name == "car1":
            pname = images(name, 300, 670, 800, 1000) ##position of car1
        elif name == "car2":
            pname = images(name, 800, 670, 1200, 1000) ##position of car2
        elif name == "car3":
            pname = images(name, 1300, 670, 1700, 1000) ##position of car3

        if pname._check():
            status="is home"
        else:
            status="is not home"
        the_data={
            "image": "output.jpg",
            "name": name,
            "status": status
        }
    else:
        return redirect(url_for('index'))
        
    return render_template('who.html', app_data=app_data, the_data=the_data, names=names)


if __name__ == '__main__':
    app.run(debug=DEVELOPMENT_ENV)
