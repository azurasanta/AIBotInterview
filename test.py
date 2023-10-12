import openai
import os
import requests
import uuid
from flask import Flask, request, jsonify, send_file, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Render the index page."""
    return render_template('room.html')

if __name__ == '__main__':
    app.run()