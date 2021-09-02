from flask import Flask

from database import db_session, init_db
from models import Project


app = Flask(__name__)
# init_db()

@app.route("/api/projects", methods=["POST"])
def add_project():
    # TODO
    # - Processar os pacotes recebidos
    # - Persistir informações no banco
    return {'foo': 'bar'}

@app.route("/api/projects/<string:project_name>", methods=["GET"])
def show_project_detail(project_name):
    # TODO
    # - Retornar informações do projeto
    return {'foo': 'bar'}

@app.route("/api/projects/<string:project_name>", methods=["DELETE"])
def delete_project(project_name):
    # TODO
    # - Apagar o projeto indicado
    return {'foo': 'bar'}

@app.teardown_appcontext
def shutdown_session(exception=None):
    # Remover sessões ao final de cada request
    db_session.remove()
