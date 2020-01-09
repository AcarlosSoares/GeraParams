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

  message = None

  objeto_sorted = {k : objeto[k] for k in sorted(objeto.keys())}
  return render_template("index.html", lista=objeto_sorted, error=message)


@app.route('/incluir', methods=['POST'])
def incluir():

  message = None

  try:
    gerarparams = request.form['gerar_params']
    if gerarparams:
      gerarParams()
      message = "Arquivo 'geragrud.cnf' gerado com sucesso!"
      objeto_sorted = {k : objeto[k] for k in sorted(objeto.keys())}
      return render_template("index.html", lista=objeto_sorted, error=message)
  except Exception as e:
    gerarparams = None

  conexao_bd = request.form['conexao_bd']
  nome_bd = request.form['nome_bd']
  nome_tabela = request.form['nome_tabela']
  nome_model = request.form['nome_model']

  if not conexao_bd:
    message = "Conexão com BD deve ser preenchido!"
    return render_template("index.html", lista=objeto, error=message)
    message = None

  if not nome_bd:
    message = "Nome do BD deve ser preenchido!"
    return render_template("index.html", lista=objeto, error=message)
    message = None

  if not nome_tabela:
    message = "Nome da tabela do BD deve ser preenchido!"
    return render_template("index.html", lista=objeto, error=message)
    message = None

  if not nome_model:
    message = "Nome da tabela do BD no Model deve ser preenchido!"
    return render_template("index.html", lista=objeto, error=message)
    message = None

  atributo = request.form['atributo']
  if not atributo:
    message = "Nome do atributo da tabela do BD deve ser preenchido!"
    return render_template("index.html", lista=objeto, error=message)
    message = None

  titulo = request.form['titulo']
  if not titulo:
    message = "Nome Titulo deve ser preenchido!"
    return render_template("index.html", lista=objeto, error=message)
    message = None

  tam_bd = request.form['tam_bd']
  if not tam_bd:
    message = "Tamanho do atributo no BD deve ser preenchido!"
    return render_template("index.html", lista=objeto, error=message)
    message = None

  tam_lista = request.form['tam_lista']
  if not tam_lista:
    message = "Tamanho do atributo na Lista de Consulta deve ser preenchido!"
    return render_template("index.html", lista=objeto, error=message)
    message = None

  tam_relat = request.form['tam_relat']
  if not tam_relat:
    message = "Tamanho do atributo na Lista do Relatório deve ser preenchido!"
    return render_template("index.html", lista=objeto, error=message)
    message = None

  val = 0
  while val in objeto:
    val += 1

  new_list ={
  'atributo':atributo,
  'pk':request.form['pk'],
  'inc':request.form['inc'],
  'alt':request.form['alt'],
  'exc':request.form['exc'],
  'tipo':request.form['tipo'],
  'titulo':titulo,
  'tam_bd':tam_bd,
  'tam_lista':tam_lista,
  'tam_relat':tam_relat}

  objeto[val] = new_list

  objeto_sorted = {k : objeto[k] for k in sorted(objeto.keys())}

  return render_template("index.html", lista=objeto_sorted, error=message)


@app.route('/excluir/<int:id>')
def excluir(id):

  message = None

  if id in objeto:
    del objeto[id]

  objeto_sorted = {k : objeto[k] for k in sorted(objeto.keys())}
  return render_template("index.html", lista=objeto_sorted, error=message)


def gerarParams():

  conexao_bd = request.form['conexao_bd']
  nome_bd = request.form['nome_bd']
  nome_tabela = request.form['nome_tabela']
  nome_model = request.form['nome_model']

  s = open("geracrud_novo.cnf","w", encoding='utf-8')

  x = "list_form_key = '@@LIST_FORM@@'" + '\n'
  x += "list_form_value = 'ListaForm'" + '\n'
  s.write(x)

  x = "insert_form_key = '@@INSERT_FORM@@'" + '\n'
  x += "insert_form_value = 'IncluiForm'" + '\n'
  s.write(x)

  x = "update_form_key = '@@UPDATE_FORM@@'" + '\n'
  x += "update_form_value = 'AlteraForm'" + '\n'
  s.write(x)

  x = "table_model_key = '@@TABLE_MODEL@@'" + '\n'
  x += "table_model_value = '" + nome_model + "'" + '\n'
  s.write(x)

  x = "database_name_key = '@@DATABASE_NAME@@'" + '\n'
  x += "database_name_value = '" + nome_bd + "'" + '\n'
  s.write(x)

  x = "table_name_key = '@@TABLE_NAME@@'" + '\n'
  x += "table_name_value = '" + nome_tabela + "'" + '\n'
  s.write(x)

  x = "" + '\n'
  s.write(x)

  x = "insert_sql_key = '@@INSERT_SQL@@'" + '\n'
  x += "update_sql_get_key = '@@UPDATE_SQL_GET@@'" + '\n'
  x += "update_sql_post_key = '@@UPDATE_SQL_POST@@'" + '\n'
  x += "print_list_key = '@@PRINT_LIST@@'" + '\n'
  x += "ordenarpor_choices_key = '@@ORDENARPOR_CHOICES@@'" + '\n'
  x += "models_attributes_key = '@@MODELS_ATTR@@'" + '\n'
  s.write(x)

  s.close()

  print("GeraCrud", "Arquivo <geragrud.cnf> gerado com sucesso!")


if __name__ == '__main__':
  app.run(debug=True)

