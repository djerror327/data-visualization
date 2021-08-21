from os import path
from flask import Flask
from flask import render_template

template_dir = path.abspath('../frontend')
app = Flask(__name__, template_folder=template_dir)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
