import pymysql
import boto3
from boto3.dynamodb.conditions import Key
from flask import Flask
from flask import render_template
from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
