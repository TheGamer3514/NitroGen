import os
try:
    import flask
except ImportError:
    os.system("pip install flask")

from flask import Flask
from threading import Thread



app = Flask('')

@app.route('/')
def home():
	return 'discord.gg/sillydev'

def run():
  app.run(
		host='0.0.0.0',
		port=3514
	)

def keep_alive():
	'''
	Creates and starts new thread that runs the function run.
	'''
	t = Thread(target=run)
	t.start()
