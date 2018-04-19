import os
import subprocess
from flask import Flask, render_template, request, send_from_directory
from final import music

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return render_template('web.html')

@app.route('/upload', methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'static/')

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        filename = file.filename
        destination = "/".join([target, filename])
        file.save(destination)

    names = music()

    return render_template("complete.html", vidname=names)

@app.route('/upload/<filename>')
def send_video(filename):
    return send_from_directory("samples", filename)