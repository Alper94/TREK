#!flask/bin/python
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"


@app.route('/download/<path:filename>')
def downloadFile (filename):
    return send_from_directory('files', filename, as_attachment=True, cache_timeout=0)

if __name__ == '__main__':
    app.run(debug=True)