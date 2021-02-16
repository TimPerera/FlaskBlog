#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 14:57:27 2021

@author: timothy
"""

from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
     'author': 'Timothy Perera',
     'title': 'Blog Post 1',
     'content': 'First post content',
     'date_posted': 'February 13, 2021'
     },
    {
     'author': 'Jane Doe',
     'title': 'Blog Post 2',
     'content': 'First post content',
     'date_posted': 'February 14, 2021'
     }
    ]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')


if __name__ == '__main__':
	app.run(debug=True)





