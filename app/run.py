# pip install Flask-Materialize

from flask import Flask, render_template
from flask_material import Material
from flask import request
from collections import OrderedDict

app = Flask(__name__)
Material(app)

dados =  {'conexao_bd':'', 'nome_bd':'', 'nome_tabela':'', 'nome_model':''}

lista = {
0 : {'atributo':'id_empresa', 'pk':'T', 'lis':'F', 'inc':'F', 'alt':'F', 'exc':'F', 'tipo':'int', 'titulo':'Seq', 'tam_bd':'10', 'tam_lista':'10', 'tam_relat':'30'},
1 : {'atributo':'ds_nomefantasia_emp','pk':'F', 'lis':'T', 'inc':'T', 'alt':'T', 'exc':'T', 'tipo':'string', 'titulo':'Nome Fantasia', 'tam_bd':'10', 'tam_lista':'10', 'tam_relat':'30'},
2 : {'atributo':'ds_razaosocial_emp', 'pk':'F', 'lis':'T', 'inc':'T', 'alt':'F', 'exc':'T', 'tipo':'string', 'titulo':'Razão Social', 'tam_bd':'10', 'tam_lista':'10', 'tam_relat':'30'},
3 : {'atributo':'ds_cnpj_emp', 'pk':'F', 'lis':'T', 'inc':'T', 'alt':'T', 'exc':'F', 'tipo':'string', 'titulo':'CNPJ', 'tam_bd':'10', 'tam_lista':'10', 'tam_relat':'30'},
4 : {'atributo':'ds_cidade_emp', 'pk':'F', 'lis':'F', 'inc':'T', 'alt':'T', 'exc':'F', 'tipo':'string', 'titulo':'Cidade', 'tam_bd':'10', 'tam_lista':'10', 'tam_relat':'30'} }


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
  'lis':request.form['lis'],
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

  x = "# 01 - utilizado na geração das rotinas do routes.py" + '\n'
  x += "route_list_form_key = '@@LIST_FORM@@'  # Delimitador do nome do form para o formulario de listagem" + '\n'
  x += "route_list_form_value = 'ListaForm' # Nome do form para o formulario de listagem" + '\n'
  x += "route_insert_form_key = '@@INSERT_FORM@@'  # Delimitador do nome do form para o formulario de inclusão" + '\n'
  x += "route_insert_form_value = 'IncluiForm' # Nome do form para o formulario de inclusão" + '\n'
  x += "route_update_form_key = '@@UPDATE_FORM@@'  # Delimitador do form para o formulario de alteração" + '\n'
  x += "route_update_form_value = 'AlteraForm' # Nome do form para o formulario de alteração" + '\n'
  x += "" + '\n'
  s.write(x)

  x = "# 02 - utilizado na geração das rotinas do routes.py" + '\n'
  x += "table_model_key = '@@TABLE_MODEL@@'  # Delimitador do nome da tabela no modelo" + '\n'
  x += "table_model_value = '" + nome_model + "'" + "  # Nome da Tabela no Modelo" + '\n'
  x += "" + '\n'
  s.write(x)

  x = "# 03 - utilizado na geração das rotinas: lista.html, inclui.html, altera.html e routes.py" + '\n'
  x += "database_name_key = '@@DATABASE_NAME@@'  # Delimitador do nome da tabela no banco de dados" + '\n'
  x += "database_name_value = '" + nome_bd + "'" + "  # Nome do Banco de Dados" + '\n'
  x += "" + '\n'
  s.write(x)

  x = "# 04 - utilizado na geração das rotinas: lista.html, inclui.html, altera.html e routes.py" + '\n'
  x += "table_name_key = '@@TABLE_NAME@@'  # Delimitador do nome da tabela no banco de dados" + '\n'
  x += "table_name_value = '" + nome_tabela + "'" + "  # Nome da Tabela no Banco de Dados" + '\n'
  x += "" + '\n'
  s.write(x)

  for key, value in lista.items():
    if value.get("pk") == 'T':
      table_pk_value = "'" + value.get("atributo") + "'"
      break

  x = "# 05 - utilizado na geração das rotinas do routes.py" + '\n'
  x += "table_pk_key = '@@TABLE_PK@@'  # Delimitador do nome da Primary Key da tabela no banco de dados" + '\n'
  x += "table_pk_value = " + table_pk_value  + "  # Nome da Primary Key da tabela no banco de dados" + '\n'
  x += "" + '\n'
  s.write(x)

  i = 0
  table_column_list = "["
  table_column_type_list = "["
  table_column_title_list = "["
  table_column_length_list = "["
  for key, value in lista.items():
    i += 1
    if i == len(lista):
      table_column_list += "'" + value.get("atributo") + "'"
      table_column_type_list += "'" + value.get("tipo") + "'"
      table_column_title_list += "'" + value.get("titulo") + "'"
      table_column_length_list += "'" + value.get("tam_bd") + "'"
    else:
      table_column_list += "'" + value.get("atributo") + "', "
      table_column_type_list += "'" + value.get("tipo") + "', "
      table_column_title_list += "'" + value.get("titulo") + "', "
      table_column_length_list += "'" + value.get("tam_bd") + "', "
  table_column_list += "]"
  table_column_type_list += "]"
  table_column_title_list += "]"
  table_column_length_list += "]"

  x = "# 06 - utilizado na criação do banco de dados" + '\n'
  x += "table_column_key = '@@TABLE_COLUMN@@'  # Delimitador do nome das colunas da tabela no banco de dados" + '\n'
  x += "table_column_list = " + table_column_list + "  # Nome dos atributos para a criação do banco de dados" + '\n'
  x += "table_column_type_list = " + table_column_type_list + "  # Lista dos tipos das colunas para a criação do banco de dados - tipos disponiveis: int, string, datetime, text, boolean" + '\n'
  x += "table_column_title_list = " + table_column_title_list + "  # Nome dos atributos para a criação do banco de dados" + '\n'
  x += "table_column_length_list = " + table_column_length_list + "  # Lista dos tamanhos das colunas para a criação do banco de dados" + '\n'
  x += "" + '\n'
  s.write(x)

  conta = 0
  for key, value in lista.items():
    if value.get("lis") == 'T':
      conta += 1

  i = 0
  search_title_column_list = "["
  search_detail_column_list = "["
  search_length_column_list = "["
  print_length_column_list = "["
  for key, value in lista.items():
    if value.get("lis") == 'T':
      i += 1
      if i == conta:
        search_title_column_list += "'" + value.get("titulo") + "'"
        search_detail_column_list += "'" + value.get("atributo") + "'"
        search_length_column_list += "'" + value.get("tam_lista") + "'"
        print_length_column_list += "'" + value.get("tam_relat") + "'"
      else:
        search_title_column_list += "'" + value.get("titulo") + "', "
        search_detail_column_list += "'" + value.get("atributo") + "', "
        search_length_column_list += "'" + value.get("tam_lista") + "', "
        print_length_column_list += "'" + value.get("tam_relat") + "', "
  search_title_column_list += "]"
  search_detail_column_list += "]"
  search_length_column_list += "]"
  print_length_column_list += "]"

  x = "# 07 - utilizado na geração no formulario de listagem em html: lista.html" + '\n'
  x += "search_title_column_key = '@@TITLE_COLUMN@@'  # Delimitador do nome dos títulos das colunas para a tela: lista.html" + '\n'
  x += "search_title_column_list = " + search_title_column_list + "  # Lista dos nomes das colunas e labels" + '\n'
  x += "search_detail_column_list = " + search_detail_column_list + "  # Nome dos atributos para a criação do banco de dados para a tela: lista.html" + '\n'
  x += "search_length_column_list = " + search_length_column_list + "  # Lista dos tamanhos das colunas para a tela: lista.html" + '\n'
  x += "print_length_column_list = " + print_length_column_list + "  # Lista dos tamanhos das colunas para o relatório" + '\n'
  x += "" + '\n'
  s.write(x)

  for key, value in lista.items():
    if value.get("exc") == 'T':
      delete_value = "'" + value.get("atributo") + "'"
      break

  x = "# 08 - utilizado na rotina de exclusão de registro no formulario de listagem em html: lista.html" + '\n'
  x += "delete_key = '@@DELETE@@'  # Delimitador do nome do atributo da tabela para a rotina de exclusão" + '\n'
  x += "delete_value = " + delete_value + "  # Nome do atributo da tabela para a rotina de exclusão" + '\n'
  x += "" + '\n'
  s.write(x)

  conta = 0
  for key, value in lista.items():
    if value.get("inc") == 'T':
      conta += 1

  i = 0
  insert_form_title_list = "["
  insert_form_list = "["
  insert_form_column_type_list = "["
  for key, value in lista.items():
    if value.get("inc") == 'T':
      i += 1
      if i == conta:
        insert_form_title_list += "'" + value.get("titulo") + "'"
        insert_form_list += "'" + value.get("atributo") + "'"
        insert_form_column_type_list += "'" + value.get("tipo") + "'"
      else:
        insert_form_title_list += "'" + value.get("titulo") + "', "
        insert_form_list += "'" + value.get("atributo") + "', "
        insert_form_column_type_list += "'" + value.get("tipo") + "', "
  insert_form_title_list += "]"
  insert_form_list += "]"
  insert_form_column_type_list += "]"

  x = "# 09 - utilizado na geração no formulario de inclusão em html: inclui.html" + '\n'
  x += "insert_form_key = '@@FORM_INSERT@@'  # Delimitador da lista de atributos para inclusão de dados no banco de dados" + '\n'
  x += "insert_form_title_list = " + insert_form_title_list + "  # Lista dos nomes das colunas para inclui.html" + '\n'
  x += "insert_form_list = " + insert_form_list + "  # Lista de atributos para inclui.html" + '\n'
  x += "insert_form_column_type_list = " + insert_form_column_type_list + "  # Lista dos tipos das colunas para a definição do formulario (forms.py)" + '\n'
  x += "" + '\n'
  s.write(x)

  conta = 0
  for key, value in lista.items():
    if value.get("alt") == 'T':
      conta += 1

  i = 0
  update_form_title_list = "["
  update_form_list = "["
  update_form_column_type_list = "["
  for key, value in lista.items():
    if value.get("alt") == 'T':
      i += 1
      if i == conta:
        update_form_title_list += "'" + value.get("titulo") + "'"
        update_form_list += "'" + value.get("atributo") + "'"
        update_form_column_type_list += "'" + value.get("tipo") + "'"
      else:
        update_form_title_list += "'" + value.get("titulo") + "', "
        update_form_list += "'" + value.get("atributo") + "', "
        update_form_column_type_list += "'" + value.get("tipo") + "', "
  update_form_title_list += "]"
  update_form_list += "]"
  update_form_column_type_list += "]"

  x = "# 10 - utilizado na geração no formulario de alteração em html: altera.html" + '\n'
  x += "update_form_key = '@@FORM_UPDATE@@'  # Delimitador da lista de atributos para atualização de dados no banco de dados" + '\n'
  x += "update_form_title_list = " + update_form_title_list + "  # Lista dos nomes das colunas para altera.html" + '\n'
  x += "update_form_list = " + update_form_list + " # Lista de atributos para altera.html" + '\n'
  x += "update_form_column_type_list = " + update_form_column_type_list + " # Lista dos tipos das colunas para a definição do formulario (forms.py)" + '\n'
  x += "" + '\n'
  s.write(x)

  x = "# 11 - utilizado na geração das rotinas do routes.py" + '\n'
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

