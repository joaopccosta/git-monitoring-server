import prometheus_client
from flask import Flask, Response, request, render_template, abort
from src.GitCLI import GitCLI
from src.Project import Project
from src.helpers.PrometheusMetrics import setupMetrics

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')
app = Flask(__name__)
gitCLI = GitCLI()
projects = {}

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/add/<name>", methods=['POST'])
def addProject(name):
    try:
        url = request.get_data().decode("utf-8")
        print(f"Fetching {url}")
        project = Project(gitCLI, name, url)
        project.fetchCommits()
        projects[name] = project
        return "200"
    except Exception as exception:
        abort(500)

@app.route("/list/<name>")
def listProject(name):
    if name not in projects:
        return render_template('error.html', projectname=name), 404
    else:
        return render_template('commits.html', projectname=name, commits=projects[name].commits.values()), 200


@app.route("/json/<name>")
def listProjectAsJson(name):
    if name not in projects:
        return render_template('error.html', projectname=name), 404
    else:
        return render_template('json.html', projectname=name, json=projects[name].toJson()), 200

@app.route('/metrics')
def metrics():
    return Response(prometheus_client.generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@app.errorhandler(500)
def handle_500(error):
    return str(error), 500

@app.errorhandler(400)
def handle_400(error):
    return str(error), 400

@app.errorhandler(404)
def handle_404(error):
    return str(error), 404

if __name__ == "__main__":
    setupMetrics(app)
    app.run(host="0.0.0.0")
