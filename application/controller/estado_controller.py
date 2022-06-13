import imp
from application.model.dao import estado_dao
from flask import render_template
from application import app
from application.model.dao.estado_dao import EstadoDao
from application.model.entity.estado import Estado


@app.route("/estado/<string:uf>")
def noticia_estado(uf):
  estado_dao = EstadoDao()
  estado_dao = Estado()
  for estado in estado_dao.get_estado_lista():
    if estado.uf == uf:
      return render_template("noticias-estado.html", estado= Estado.get_noticia_lista(estado.uf))
  return render_template("noticias-estado.html", estados=estado_dao.get_estado_lista())
