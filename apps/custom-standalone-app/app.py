from flask import Flask, request, render_template, abort
import os

app = Flask(__name__)
alpha_enabled = os.environ.get('ENABLE_ALPHA')

@app.route('/')
def hello():
    return render_template('index.html', alpha_enabled=alpha_enabled)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)