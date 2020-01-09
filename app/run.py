# pip install Flask-Materialize

from flask import Flask, render_template
from flask_material import Material
from flask import request
from collections import OrderedDict

app = Flask(__name__)
Material(app)

objeto = {
0 : {'atributo':'id_empresa', 'pk':'T', 'inc':'F', 'alt':'F', 'exc':'F', 'tipo':'Int', 'titulo':'Seq', 'tam_bd':'10', 'tam_lista':'10', 'tam_relat':'30'},
1 : {'atributo':'ds_nomefantasia_emp','pk':'F', 'inc':'F', 'alt':'F', 'exc':'F', 'tipo':'String', 'titulo':'Nome Fantasia', 'tam_bd':'10', 'tam_lista':'10', 'tam_relat':'30'},
2 : {'atributo':'ds_razaosocial_emp', 'pk':'F', 'inc':'F', 'alt':'F', 'exc':'F', 'tipo':'String', 'titulo':'Razão Social', 'tam_bd':'10', 'tam_lista':'10', 'tam_relat':'30'},
3 : {'atributo':'ds_cnpj_emp', 'pk':'F', 'inc':'F', 'alt':'F', 'exc':'F', 'tipo':'String', 'titulo':'CNPJ', 'tam_bd':'10', 'tam_lista':'10', 'tam_relat':'30'},
4 : {'atributo':'ds_cidade_emp', 'pk':'F', 'inc':'F', 'alt':'F', 'exc':'F', 'tipo':'String', 'titulo':'Cidade', 'tam_bd':'10', 'tam_lista':'10', 'tam_relat':'30'} }

@app.route('/')
def index():

  return render_template("index.html", lista=objeto)


@app.route('/incluir', methods=['POST'])
def incluir():

  val = 1
  while val in objeto:
    val += 1

  new_list ={
  'atributo':request.form['atributo'],
  'pk':request.form['pk'],
  'inc':request.form['inc'],
  'alt':request.form['alt'],
  'exc':request.form['exc'],
  'tipo':request.form['tipo'],
  'titulo':request.form['titulo'],
  'tam_bd':request.form['tam_bd'],
  'tam_lista':request.form['tam_lista'],
  'tam_relat':request.form['tam_relat']}

  objeto[val] = new_list

  objeto_sorted = {k : objeto[k] for k in sorted(objeto.keys())}

  return render_template("index.html", lista=objeto_sorted)


@app.route('/excluir/<int:id>')
def excluir(id):

  if id in objeto:
    del objeto[id]

  objeto_sorted = {k : objeto[k] for k in sorted(objeto.keys())}

  return render_template("index.html", lista=objeto_sorted)


if __name__ == '__main__':
  app.run(debug=True)

