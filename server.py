from flask import Flask, request, render_template
from src.GitCLI import GitCLI
from src.Project import Project

app = Flask(__name__)
gitCLI = GitCLI()
projects = {}
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/add/<name>", methods=['POST'])
def addProject(name):
    url = request.get_data().decode("utf-8")
    print(f"Fetching {url}")
    project = Project(gitCLI, name, url)
    project.fetchCommits()
    projects[name] = project
    return "200"

@app.route("/list/<name>")
def listProject(name):
    if name not in projects:
        return render_template('error.html', projectname=name)
    else:
        return render_template('commits.html', projectname=name, commits=projects[name].commits.values())


@app.route("/json/<name>")
def listProjectAsJson(name):
    if name not in projects:
        return render_template('error.html', projectname=name)
    else:
        return render_template('json.html', projectname=name, json=projects[name].toJson())

if __name__ == "__main__":
    app.run(host="0.0.0.0")