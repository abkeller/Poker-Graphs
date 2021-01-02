import os
import datetime as dt
import pandas as pd
from poker_graph import player_data
import pygal
import time

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
	"""Show portfolio of stocks"""
	players, number_of_hands = player_data()

	line_chart = pygal.Line()
	line_chart.title = "Chips by Hand"

	for i in range(number_of_hands):
		if i <= 20:
			lower = 0
		else:
			lower = i - 20

		line_chart.x_labels = map(str, range(lower, i))

		for player in players:
			line_chart.add(player, players[player][lower:i])

		return line_chart.render_response()

		return render_template("index.html")



def make_graph(line_chart):
		
		return line_chart.render_response()
		return render_template("index.html", chart = chart)
