from flask import Flask, request, render_template, abort
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
    return "200"


@app.route("/json/<name>")
def listProjectAsJson(name):
    return "200"

if __name__ == "__main__":
    app.run()