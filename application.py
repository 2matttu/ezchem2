# Matt Tu
# CS50 Final Project
# application.py for EZ Chem app
# deleted ikp3db==1.4 in requirements.txt to make Heroku build work
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
        n = request.form.get("n")  # how many chemicals (rows) users want in their table
        if not n:
            return render_template("index.html")
        rows = int(n)
        nums = range(rows)
        strings = []
        for i in range(len(nums)):
            strings.append(str(nums[i]))
            # creates a list of n numbers casted as strings form 0 to n-1.
            # i.e. if the user wants 5 rows the list would be ["0","1","2","3","4"]
            # this will come be used with Jinja to create forms with a variable amount rows.
        return render_template("form.html", strings=strings)


@app.route('/form', methods=["GET", "POST"])
def form():
    if request.method == "GET":
        return redirect('/')
    if request.method == "POST":
        data = []
        sublist = []
        index = 0
        while True:
            # places form data into a list of lists, with each parent list element is a chemical, and the each child list element is
            # ...one property of the chemical
            for j in range(9):
                sublist.append(request.form.get(PROPERTIES[j] + str(index)))
            data.append(sublist)
            sublist = []
            if request.form.get("name" + str(index+1)) == None:
                # if the value of name<x> is None, that means that there are no chemicals left in the form, meaning all the form
                # ...rows are accounted for in the list, so render_template is called.
                return render_template("table.html", data=data)
            index = index + 1
