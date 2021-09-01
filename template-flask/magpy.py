from flask import Flask

from database import db_session, init_db
from models import Project


app = Flask(__name__)
init_db()

@app.route("/api/projects", methods=["POST"])
def add_project():
    project = Project(id="1", name="teste")
    db_session.add(project)
    db_session.commit()
    return {'foo': 'bar'}

@app.route("/api/projects/<string:project_name>", methods=["GET"])
def show_project_detail(project_name):
    result = Project.query.filter_by(name='teste').first()
    print(result)
    return {'foo': 'bar'}

@app.route("/api/projects/<string:project_name>", methods=["DELETE"])
def delete_project(project_name):
    result = Project.query.filter_by(name='teste').first()
    db_session.delete(result)
    db_session.commit()
    return {'foo': 'bar'}

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
