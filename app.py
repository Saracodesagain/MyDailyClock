from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')  # Theme selector


@app.route('/indexolive')
def index_olive():
    return render_template('indexolive.html')


@app.route('/indexcute')
def index_cute():
    return render_template('indexcute.html')  # optional for pink version


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

print(app.url_map)

