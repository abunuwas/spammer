from flask import Flask
from flask import render_template, abort, redirect, url_for, request

from os.path import expanduser 

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('hello.html')

@app.route("/sendMetrics")
def log_metric():
	metric = request.args.get('metric_name')
	value = request.args.get('metric_value')
	return '{} = {}'.format(metric, value)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6060)
