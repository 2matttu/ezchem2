# application.py
# deleted ikp3db==1.4
import os

from flask import Flask, flash, jsonify, redirect, render_template, request, session

PROPERTIES = ["name", "formula", "mw", "mp", "bp", "density", "amt", "hazards", "precautions"]

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

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
            if request.form.get("name" + str(index+1)) == None:
                return render_template("table.html", data = data)
            index = index + 1
