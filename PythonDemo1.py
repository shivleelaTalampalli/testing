# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 15:32:01 2023

@author: shivl
""" 
from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Hello! This is the Main Page <h1>HELLO<h1>"

if __name__ == "__main__":
        app.run()
        