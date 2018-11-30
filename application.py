# application.py
# deleted ikp3db==1.4
import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

PROPERTIES = ["name", "formula", "mw", "mp", "bp", "density", "amt", "hazards", "precautions"]

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        n = request.form.get("n")
        if not n:
            return render_template("index.html")
        rows = int(n)
        nums = range(rows)
        strings = []
        for i in range(len(nums)):
            strings.append(str(nums[i]))
        return render_template("form.html", strings = strings)

@app.route('/form', methods= ["GET", "POST"])
def form():
    if request.method == "GET":
        return redirect('/')
    if request.method == "POST":
        data = []
        sublist = []
        index = 0
        while True:
            for j in range(9):
                sublist.append(request.form.get(PROPERTIES[j] + str(index)))
            data.append(sublist)
            sublist = []
            if not request.form.get("name" + str(index+1)):
                return render_template("table.html", data = data)
            index = index + 1
