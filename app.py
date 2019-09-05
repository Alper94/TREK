#!flask/bin/python
from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/download')
def downloadFile ():
    path = "D:/File.txt"
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)