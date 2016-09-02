from flask import Flask
from flask import render_template, abort, redirect, url_for, request

import random
import time

from create_cluster import test_metric_alarm, describe_cluster, list_clusters

app = Flask(__name__)


@app.route("/")
def main():
	clusters = [cluster.split('/')[1] for cluster in list_clusters()]
	details = request.args.get('details', None)
	return render_template('hello.html', clusters=clusters, details=details)

@app.route("/testScaleUp")
def test_scaleup():
	high_values = (random.randint(51,100) for i in range(65))
	test_metric_alarm(namespace='xmpp_component', metric_name='queue_size', metric_values=high_values, alarm='xmpp_component_queue_size_increase')
	time.sleep(len(list(high_values))+1)
	return redirect(url_for("cluster_detail", cluster='xmpp_component_cluster'))

@app.route("/describeCluster")
def cluster_detail():
	cluster = request.args.get('cluster')
	details = describe_cluster(cluster)
	return render_template("hello.html", details=details)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=6060)
