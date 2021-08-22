import json
from os import path

from flask import Flask
from flask import render_template

from services.log_analyser import get_chart_data

template_dir = path.abspath('../frontend')
app = Flask(__name__, template_folder=template_dir)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/log_chart', methods=['GET'])
def log_chart_json():
    json_formatted = json.dumps(get_chart_data())
    return json_formatted


@app.route('/log', methods=['GET'])
def log_page():
    return render_template('log.html')


if __name__ == '__main__':
    app.run()
