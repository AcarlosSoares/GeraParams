# pip install Flask-Materialize

from flask import Flask, render_template
from flask_material import Material
from flask import request
from collections import OrderedDict

app = Flask(__name__)
Material(app)

dados =  {'conexao_bd':'', 'nome_bd':'', 'nome_tabela':'', 'nome_model':''}

lista = {
0 : {'atributo':'id_empresa', 'pk':'T', 'inc':'F', 'alt':'F', 'exc':'F', 'tipo':'Int', 'titulo':'Seq', 'tam_bd':'10', 'tam_lista':'10', 'tam_relat':'30'},
1 : {'atributo':'ds_nomefantasia_emp','pk':'F', 'inc':'F', 'alt':'F', 'exc':'F', 'tipo':'String', 'titulo':'Nome Fantasia', 'tam_bd':'10', 'tam_lista':'10', 'tam_relat':'30'},
2 : {'atributo':'ds_razaosocial_emp', 'pk':'F', 'inc':'F', 'alt':'F', 'exc':'F', 'tipo':'String', 'titulo':'Razão Social', 'tam_bd':'10', 'tam_lista':'10', 'tam_relat':'30'},
3 : {'atributo':'ds_cnpj_emp', 'pk':'F', 'inc':'F', 'alt':'F', 'exc':'F', 'tipo':'String', 'titulo':'CNPJ', 'tam_bd':'10', 'tam_lista':'10', 'tam_relat':'30'},
4 : {'atributo':'ds_cidade_emp', 'pk':'F', 'inc':'F', 'alt':'F', 'exc':'F', 'tipo':'String', 'titulo':'Cidade', 'tam_bd':'10', 'tam_lista':'10', 'tam_relat':'30'} }

# for key, value in lista.items():
#   print(key, value)
#   print(value.get("atributo"))

# for key, value in lista.items():
#   if "pk" in value:
#     print(value.get("atributo"))

# for key, value in lista.items():
#   print(value.get("pk"))

# for key, value in lista.items():
#   print(lista[key]["pk"])

# lista.keys()
# lista.values()
# lista.items()

# atributos = []
# for key, value in lista.items():
#   atributos.append(value.get("atributo"))


@app.route('/')
def index():

  message = None

  lista_sorted = {k : lista[k] for k in sorted(lista.keys())}
  return render_template("index.html", dados=dados, lista=lista_sorted, error=message)


@app.route('/incluir', methods=['POST'])
def incluir():

  message = None

  try:
    gerarparams = request.form['gerar_params']
    if gerarparams:
      gerarParams()
      message = "Arquivo 'geragrud.cnf' gerado com sucesso!"
      lista_sorted = {k : lista[k] for k in sorted(lista.keys())}
      return render_template("index.html", dados=dados, lista=lista_sorted, error=message)
  except Exception as e:
    gerarparams = None

  conexao_bd = request.form['conexao_bd']
  nome_bd = request.form['nome_bd']
  nome_tabela = request.form['nome_tabela']
  nome_model = request.form['nome_model']

  if not conexao_bd:
    message = "Conexão com BD deve ser preenchido!"
    return render_template("index.html", dados=dados, lista=lista, error=message)
    message = None

  if not nome_bd:
    message = "Nome do BD deve ser preenchido!"
    return render_template("index.html", dados=dados, lista=lista, error=message)
    message = None

  if not nome_tabela:
    message = "Nome da tabela do BD deve ser preenchido!"
    return render_template("index.html", dados=dados, lista=lista, error=message)
    message = None

  if not nome_model:
    message = "Nome da tabela do BD no Model deve ser preenchido!"
    return render_template("index.html", dados=dados, lista=lista, error=message)
    message = None

  atributo = request.form['atributo']
  if not atributo:
    message = "Nome do atributo da tabela do BD deve ser preenchido!"
    return render_template("index.html", dados=dados, lista=lista, error=message)
    message = None

  titulo = request.form['titulo']
  if not titulo:
    message = "Nome Titulo deve ser preenchido!"
    return render_template("index.html", dados=dados, lista=lista, error=message)
    message = None

  tam_bd = request.form['tam_bd']
  if not tam_bd:
    message = "Tamanho do atributo no BD deve ser preenchido!"
    return render_template("index.html", dados=dados, lista=lista, error=message)
    message = None

  tam_lista = request.form['tam_lista']
  if not tam_lista:
    message = "Tamanho do atributo na Lista de Consulta deve ser preenchido!"
    return render_template("index.html", dados=dados, lista=lista, error=message)
    message = None

  tam_relat = request.form['tam_relat']
  if not tam_relat:
    message = "Tamanho do atributo na Lista do Relatório deve ser preenchido!"
    return render_template("index.html", dados=dados, lista=lista, error=message)
    message = None

  val = 0
  while val in lista:
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

  dados['conexao_bd'] =  conexao_bd
  dados['nome_bd'] =  nome_bd
  dados['nome_tabela'] =  nome_tabela
  dados['nome_model'] =  nome_model

  lista[val] = new_list

  lista_sorted = {k : lista[k] for k in sorted(lista.keys())}

  return render_template("index.html", dados=dados, lista=lista_sorted, error=message)


@app.route('/excluir/<int:id>')
def excluir(id):

  message = None

  if id in lista:
    del lista[id]

  lista_sorted = {k : lista[k] for k in sorted(lista.keys())}
  return render_template("index.html", dados=dados, lista=lista_sorted, error=message)


def gerarParams():

  conexao_bd = request.form['conexao_bd']
  nome_bd = request.form['nome_bd']
  nome_tabela = request.form['nome_tabela']
  nome_model = request.form['nome_model']

  dados['conexao_bd'] =  conexao_bd
  dados['nome_bd'] =  nome_bd
  dados['nome_tabela'] =  nome_tabela
  dados['nome_model'] =  nome_model

  s = open("geracrud_novo.cnf","w", encoding='utf-8')


  x = "# utilizado na geração das rotinas do routes.py" + '\n'
  x += "route_list_form_key = '@@LIST_FORM@@'  # Delimitador do nome do form para o formulario de listagem" + '\n'
  x += "route_list_form_value = 'ListaForm' # Nome do form para o formulario de listagem" + '\n'
  x += "route_insert_form_key = '@@INSERT_FORM@@'  # Delimitador do nome do form para o formulario de inclusão" + '\n'
  x += "route_insert_form_value = 'IncluiForm' # Nome do form para o formulario de inclusão" + '\n'
  x += "route_update_form_key = '@@UPDATE_FORM@@'  # Delimitador do form para o formulario de alteração" + '\n'
  x += "route_update_form_value = 'AlteraForm' # Nome do form para o formulario de alteração" + '\n'
  x += "" + '\n'
  s.write(x)

  x = "# utilizado na geração das rotinas do routes.py" + '\n'
  x += "table_model_key = '@@TABLE_MODEL@@'  # Delimitador do nome da tabela no modelo" + '\n'
  x += "table_model_value = '" + nome_model + "'" + "  # Nome da Tabela no Modelo" + '\n'
  x += "" + '\n'
  s.write(x)

  x = "# utilizado na geração das rotinas: lista.html, inclui.html, altera.html e routes.py" + '\n'
  x += "database_name_key = '@@DATABASE_NAME@@'  # Delimitador do nome da tabela no banco de dados" + '\n'
  x += "database_name_value = '" + nome_bd + "'" + "  # Nome do Banco de Dados" + '\n'
  x += "" + '\n'
  s.write(x)

  x = "# utilizado na geração das rotinas: lista.html, inclui.html, altera.html e routes.py" + '\n'
  x += "table_name_key = '@@TABLE_NAME@@'  # Delimitador do nome da tabela no banco de dados" + '\n'
  x += "table_name_value = '" + nome_tabela + "'" + "  # Nome da Tabela no Banco de Dados" + '\n'
  x += "" + '\n'
  s.write(x)

  x = "# utilizado na geração das rotinas do routes.py" + '\n'
  x += "table_pk_key = '@@TABLE_PK@@'  # Delimitador do nome da Primary Key da tabela no banco de dados" + '\n'
  x += "table_pk_value = 'id_empresa' # Nome da Primary Key da tabela no banco de dados" + '\n'
  x += "" + '\n'
  s.write(x)


  i = 0
  table_column_list = "["
  for key, value in lista.items():
    i += 1
    if i == len(lista):
      table_column_list += "'" + value.get("atributo") + "'"
    else:
      table_column_list += "'" + value.get("atributo") + "', "
  table_column_list += "]"

  i = 0
  table_column_type_list = "["
  for key, value in lista.items():
    i += 1
    if i == len(lista):
      table_column_type_list += "'" + value.get("tipo") + "'"
    else:
      table_column_type_list += "'" + value.get("tipo") + "', "
  table_column_type_list += "]"

  i = 0
  table_column_title_list = "["
  for key, value in lista.items():
    i += 1
    if i == len(lista):
      table_column_title_list += "'" + value.get("titulo") + "'"
    else:
      table_column_title_list += "'" + value.get("titulo") + "', "
  table_column_title_list += "]"

  i = 0
  table_column_length_list = "["
  for key, value in lista.items():
    i += 1
    if i == len(lista):
      table_column_length_list += "'" + value.get("tam_bd") + "'"
    else:
      table_column_length_list += "'" + value.get("tam_bd") + "', "
  table_column_length_list += "]"

  x = "# utilizado na criação do banco de dados" + '\n'
  x += "table_column_key = '@@TABLE_COLUMN@@'  # Delimitador do nome das colunas da tabela no banco de dados" + '\n'
  x += "table_column_list = " + table_column_list + "  # Nome dos atributos para a criação do banco de dados" + '\n'
  x += "table_column_type_list = " + table_column_type_list + "  # Lista dos tipos das colunas para a criação do banco de dados - tipos disponiveis: int, string, datetime, text, boolean" + '\n'
  x += "table_column_title_list = " + table_column_title_list + "  # Nome dos atributos para a criação do banco de dados" + '\n'
  x += "table_column_length_list = " + table_column_length_list + "  # Lista dos tamanhos das colunas para a criação do banco de dados" + '\n'
  x += "" + '\n'
  s.write(x)


  x = "# utilizado na geração das rotinas do routes.py" + '\n'
  x += "insert_sql_key = '@@INSERT_SQL@@'  # Delimitador para montar os campos do insert no banco de dados da função inserir" + '\n'
  x += "update_sql_get_key = '@@UPDATE_SQL_GET@@'  # Delimitador para montar os campos do update do metodo GET da função alterar" + '\n'
  x += "update_sql_post_key = '@@UPDATE_SQL_POST@@'  # Delimitador para montar os campos do update do metodo POST da função alterar" + '\n'
  x += "print_list_key = '@@PRINT_LIST@@'  # Delimitador para montar os campos do relatório" + '\n'
  x += "ordenarpor_choices_key = '@@ORDENARPOR_CHOICES@@'  # Delimitador para montar o ordenarpor_choices do forms.py" + '\n'
  x += "models_attributes_key = '@@MODELS_ATTR@@'  # Delimitador para montar a lista de atributos do model.py" + '\n'
  x += "" + '\n'
  s.write(x)

  s.close()

  print("GeraCrud", "Arquivo <geragrud.cnf> gerado com sucesso!")


if __name__ == '__main__':
  app.run(debug=True)

