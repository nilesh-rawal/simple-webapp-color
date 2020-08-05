import os
from flask import Flask
from flask import render_template
import socket
import random
import os

app = Flask(__name__)

color_codes = {
    "red": "#CD5C5C",
    "green": "#27AE60",
    "blue": "#85C1E9",
    "blue2": "#1F618D",
    "grey": "#85929E",
    "darkblue": "#130f40"
}

color = os.environ.get('APP_COLOR') or random.choice(["grey","blue","green","red","darkblue","blue2"])

@app.route("/")
def main():
    #return 'Hello'
    print(color)
    return render_template('hello.html', name=socket.gethostname(), color=color_codes[color])

@app.route('/color/<new_color>')
def new_color(new_color):
    return render_template('hello.html', name=socket.gethostname(), color=color_codes[new_color])

@app.route('/read_file')
def read_file():
    f = open("/data/testfile.txt")
    contents = f.read()
    return render_template('hello.html', name=socket.gethostname(), contents=contents, color=color_codes[color])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
