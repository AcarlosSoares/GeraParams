# pip install Flask-Materialize

from flask import Flask, render_template
from flask_material import Material

app = Flask(__name__)
Material(app)

lista = [
{'key':'0', 'atributo':'id_empresa',          'pk':'T', 'inc':'F', 'alt':'F', 'exc':'F', 'tipo':'Int',    'titulo':'Seq',           'tam_bd':'10', 'tam_lista':'10', 'tam_relat':'30'},
{'key':'1', 'atributo':'ds_nomefantasia_emp', 'pk':'F', 'inc':'F', 'alt':'F', 'exc':'F', 'tipo':'String', 'titulo':'Nome Fantasia', 'tam_bd':'10', 'tam_lista':'10', 'tam_relat':'30'},
{'key':'2', 'atributo':'ds_razaosocial_emp',  'pk':'F', 'inc':'F', 'alt':'F', 'exc':'F', 'tipo':'String', 'titulo':'Razão Social',  'tam_bd':'10', 'tam_lista':'10', 'tam_relat':'30'},
{'key':'3', 'atributo':'ds_cnpj_emp',         'pk':'F', 'inc':'F', 'alt':'F', 'exc':'F', 'tipo':'String', 'titulo':'CNPJ',          'tam_bd':'10', 'tam_lista':'10', 'tam_relat':'30'},
{'key':'4', 'atributo':'ds_cidade_emp',       'pk':'F', 'inc':'F', 'alt':'F', 'exc':'F', 'tipo':'String', 'titulo':'Cidade',        'tam_bd':'10', 'tam_lista':'10', 'tam_relat':'30'}
]

@app.route('/')
def index():
  return render_template("index.html", lista=lista)


@app.route('/incluir')
def incluir():

  val = len(lista)
  new_list = {'key': val, 'atributo':'ds_teste', 'pk':'F', 'inc':'F', 'alt':'F', 'exc':'F', 'tipo':'String', 'titulo':'Teste', 'tam_bd':'10', 'tam_lista':'10', 'tam_relat':'30'}

  print(new_list)
  lista.append(new_list)
  return render_template("index.html", lista=lista)


@app.route('/delete/<int:id>')
def delete(id):

  conta = 0
  for i in range(len(lista)):
    if lista[i] == id:
      conta += 1

  if conta > 0:
    lista.pop(id)
  return render_template("index.html", lista=lista)


@app.route('/excluir')
def excluir():
  lista.pop(1)
  return render_template("index.html", lista=lista)

if __name__ == '__main__':
  app.run(debug=True)

