from flask import Flask, render_template
import random

app = Flask(__name__)

images = [
    'static/1.jpg',
    'static/2.jpg',
    'static/3.jpg',
    'static/4.jpg',
    'static/5.jpg',
    'static/6.jpg',
    'static/7.jpg',
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

@app.route('/static/<path:file>')
def handle_static(file):
    return send_from_directory('static', file)

if __name__ == "__main__":
    app.run(host="0.0.0.0")