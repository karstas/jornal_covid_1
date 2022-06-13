from flask import render_template
from application import app
from application.model.dao.estado_dao import EstadoDao
estado_dao = EstadoDao()


@app.route("/")
def home():
    estados_lista = estado_dao.get_estado_lista()
    return render_template("home.html", estados=estados_lista)