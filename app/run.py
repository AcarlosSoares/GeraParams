# pip install Flask-Materialize

from flask import Flask, render_template
from flask_material import Material
from flask import request
from collections import OrderedDict
from os import path
import re
import geracrud

app = Flask(__name__)
Material(app)

dados =  {'conexao_bd':'', 'nome_bd':'', 'nome_tabela':'', 'nome_model':''}

# lista = {
# }

nova_lista = {
      'key' : '',
      'atributo': '',
      'pk': '',
      'lis': '',
      'inc': '',
      'alt': '',
      'exc': '',
      'tipo': '',
      'titulo': '',
      'tam_bd': '',
      'tam_lista': '',
      'tam_relat': ''
    }


lista = {
0 : {'atributo':'id_empresa', 'pk':'T', 'lis':'F', 'inc':'F', 'alt':'F', 'exc':'F', 'tipo':'int', 'titulo':'Seq', 'tam_bd':'10', 'tam_lista':'10', 'tam_relat':'30'},
1 : {'atributo':'ds_nomefantasia_emp','pk':'F', 'lis':'T', 'inc':'T', 'alt':'T', 'exc':'T', 'tipo':'string', 'titulo':'Nome Fantasia', 'tam_bd':'10', 'tam_lista':'10', 'tam_relat':'30'},
2 : {'atributo':'ds_razaosocial_emp', 'pk':'F', 'lis':'T', 'inc':'T', 'alt':'F', 'exc':'T', 'tipo':'string', 'titulo':'Razão Social', 'tam_bd':'10', 'tam_lista':'10', 'tam_relat':'30'},
3 : {'atributo':'ds_cnpj_emp', 'pk':'F', 'lis':'T', 'inc':'T', 'alt':'T', 'exc':'F', 'tipo':'string', 'titulo':'CNPJ', 'tam_bd':'10', 'tam_lista':'10', 'tam_relat':'30'},
4 : {'atributo':'ds_cidade_emp', 'pk':'F', 'lis':'F', 'inc':'T', 'alt':'T', 'exc':'F', 'tipo':'string', 'titulo':'Cidade', 'tam_bd':'10', 'tam_lista':'10', 'tam_relat':'30'} }


@app.route('/')
def index():

  message = None

  lista.clear()

  lista_sorted = {k : lista[k] for k in sorted(lista.keys())}
  return render_template("index.html", dados=dados, lista=lista_sorted, nova_lista=nova_lista, error=message)


@app.route('/processar_atributo', methods=['GET', 'POST'])
def processar_atributo():

  nome_tabela = request.form['nome_tabela']
  if nome_tabela:
    nome_arquivo = "geracrud_" + nome_tabela + ".cnf"
  else:
    nome_arquivo = "geracrud.cnf"

  message = None

  try:
    gerar_params = request.form['gerar_params']
    if gerar_params:
      message = criticaDados()
      if message:
        return render_template("index.html", dados=dados, lista=lista, nova_lista=nova_lista, error=message)
      gerarParams(nome_arquivo)
      message = "Arquivo '" + nome_arquivo + "' gerado com sucesso!"
      lista_sorted = {k : lista[k] for k in sorted(lista.keys())}
      return render_template("index.html", dados=dados, lista=lista_sorted, nova_lista=nova_lista, error=message)
  except Exception as e:
    gerar_params = None

  try:
    carregar_params = request.form['carregar_params']
    if carregar_params:
      if path.exists(nome_arquivo):
        carregarParams(nome_arquivo)
        message = "Arquivo '" + nome_arquivo + "' carregado com sucesso!"
      else:
        message = "Falha na carga do arquivo: '" + nome_arquivo
      lista_sorted = {k : lista[k] for k in sorted(lista.keys())}
      return render_template("index.html", dados=dados, lista=lista_sorted, nova_lista=nova_lista, error=message)
  except Exception as e:
    carregar_params = None

  try:
    alterar_atributo = request.form['alterar_atributo']
    if alterar_atributo:
      message = criticaAtributos()
      if message:
        return render_template("index.html", dados=dados, lista=lista, nova_lista=nova_lista, error=message)
      id_key = request.form['key']
      alterarAtributo(id_key)
      message = "Atributo alterado com sucesso!"
      lista_sorted = {k : lista[k] for k in sorted(lista.keys())}
      return render_template("index.html", dados=dados, lista=lista_sorted, nova_lista=nova_lista, error=message)
  except Exception as e:
    alterar_atributo = None

  try:
    incluir_atributo = request.form['incluir_atributo']
    if incluir_atributo:
      message = criticaAtributos()
      if message:
        return render_template("index.html", dados=dados, lista=lista, nova_lista=nova_lista, error=message)
      incluirAtributo()
      message = "Atributo incluído com sucesso!"
      lista_sorted = {k : lista[k] for k in sorted(lista.keys())}
      return render_template("index.html", dados=dados, lista=lista_sorted, nova_lista=nova_lista, error=message)
  except Exception as e:
    incluir_atributo = None

  try:
    gerar_crud = request.form['gerar_crud']
    if gerar_crud:
      message = criticaDados()
      if message:
        return render_template("index.html", dados=dados, lista=lista, nova_lista=nova_lista, error=message)

      if path.exists(nome_arquivo):
        gerarCrud(nome_arquivo)
        message = "CRUD gerado com sucesso!"
      else:
        message = "Falha na geração do CRUD!"

      lista_sorted = {k : lista[k] for k in sorted(lista.keys())}
      return render_template("index.html", dados=dados, lista=lista_sorted, nova_lista=nova_lista, error=message)

  except Exception as e:
    gerar_crud = None


  lista_sorted = {k : lista[k] for k in sorted(lista.keys())}
  return render_template("index.html", dados=dados, lista=lista_sorted, nova_lista=nova_lista, error=message)


def incluirAtributo():

  val = 0
  while val in lista:
    val += 1

  new_list = {
    # 'key' : '',
    'atributo': request.form['atributo'],
    'pk': request.form['pk'],
    'lis': request.form['lis'],
    'inc': request.form['inc'],
    'alt': request.form['alt'],
    'exc': request.form['exc'],
    'tipo': request.form['tipo'],
    'titulo': request.form['titulo'],
    'tam_bd': request.form['tam_bd'],
    'tam_lista': request.form['tam_lista'],
    'tam_relat': request.form['tam_relat']
  }

  lista[val] = new_list


@app.route('/excluir_atributo/<int:id>')
def excluir_atributo(id):

  message = None

  if id in lista:
    del lista[id]

  lista_sorted = {k : lista[k] for k in sorted(lista.keys())}
  return render_template("index.html", dados=dados, lista=lista_sorted, nova_lista=nova_lista, error=message)


@app.route('/editar_atributo/<int:id>')
def editar_atributo(id):

  message = None

  if id in lista:
    nova_lista = {
      'key' : id,
      'atributo': lista[id]['atributo'],
      'pk': lista[id]['pk'],
      'lis': lista[id]['lis'],
      'inc': lista[id]['inc'],
      'alt': lista[id]['alt'],
      'exc': lista[id]['exc'],
      'tipo': lista[id]['tipo'],
      'titulo': lista[id]['titulo'],
      'tam_bd': lista[id]['tam_bd'],
      'tam_lista': lista[id]['tam_lista'],
      'tam_relat': lista[id]['tam_relat']
    }

  lista_sorted = {k : lista[k] for k in sorted(lista.keys())}
  return render_template("index.html", dados=dados, lista=lista_sorted, nova_lista=nova_lista, error=message)


def alterarAtributo(id):

  message = None

  if int(id) in lista:
    new_list = {
      'atributo': request.form['atributo'],
      'pk': request.form['pk'],
      'lis': request.form['lis'],
      'inc': request.form['inc'],
      'alt': request.form['alt'],
      'exc': request.form['exc'],
      'tipo': request.form['tipo'],
      'titulo': request.form['titulo'],
      'tam_bd': request.form['tam_bd'],
      'tam_lista': request.form['tam_lista'],
      'tam_relat': request.form['tam_relat']
    }

    lista[int(id)] = new_list


def gerarParams(nome_arquivo):

  conexao_bd = request.form['conexao_bd']
  nome_bd = request.form['nome_bd']
  nome_tabela = request.form['nome_tabela']
  nome_model = request.form['nome_model']

  dados['conexao_bd'] =  conexao_bd
  dados['nome_bd'] =  nome_bd
  dados['nome_tabela'] =  nome_tabela
  dados['nome_model'] =  nome_model

  s = open(nome_arquivo,"w", encoding='utf-8')

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

  table_pk_value = listaToString2("pk", "atributo")

  x = "# 05 - utilizado na geração das rotinas do routes.py" + '\n'
  x += "table_pk_key = '@@TABLE_PK@@'  # Delimitador do nome da Primary Key da tabela no banco de dados" + '\n'
  x += "table_pk_value = " + table_pk_value  + "  # Nome da Primary Key da tabela no banco de dados" + '\n'
  x += "" + '\n'
  s.write(x)

  table_column_list = listaToString1("atributo")
  table_column_type_list = listaToString1("tipo")
  table_column_title_list = listaToString1("titulo")
  table_column_length_list = listaToString1("tam_bd")

  x = "# 06 - utilizado na criação do banco de dados" + '\n'
  x += "table_column_key = '@@TABLE_COLUMN@@'  # Delimitador do nome das colunas da tabela no banco de dados" + '\n'
  x += "table_column_list = " + table_column_list + "  # Nome dos atributos para a criação do banco de dados" + '\n'
  x += "table_column_type_list = " + table_column_type_list + "  # Lista dos tipos das colunas para a criação do banco de dados - tipos disponiveis: int, string, datetime, text, boolean" + '\n'
  x += "table_column_title_list = " + table_column_title_list + "  # Nome dos atributos para a criação do banco de dados" + '\n'
  x += "table_column_length_list = " + table_column_length_list + "  # Lista dos tamanhos das colunas para a criação do banco de dados" + '\n'
  x += "" + '\n'
  s.write(x)

  search_title_column_list = listaToString("lis", "titulo")
  search_detail_column_list = listaToString("lis", "atributo")
  search_length_column_list = listaToString("lis", "tam_lista")
  print_length_column_list = listaToString("lis", "tam_relat")

  x = "# 07 - utilizado na geração no formulario de listagem em html: lista.html" + '\n'
  x += "search_title_column_key = '@@TITLE_COLUMN@@'  # Delimitador do nome dos títulos das colunas para a tela: lista.html" + '\n'
  x += "search_title_column_list = " + search_title_column_list + "  # Lista dos nomes das colunas e labels" + '\n'
  x += "search_detail_column_list = " + search_detail_column_list + "  # Nome dos atributos para a criação do banco de dados para a tela: lista.html" + '\n'
  x += "search_length_column_list = " + search_length_column_list + "  # Lista dos tamanhos das colunas para a tela: lista.html" + '\n'
  x += "print_length_column_list = " + print_length_column_list + "  # Lista dos tamanhos das colunas para o relatório" + '\n'
  x += "" + '\n'
  s.write(x)

  delete_value = listaToString2("exc", "atributo")

  x = "# 08 - utilizado na rotina de exclusão de registro no formulario de listagem em html: lista.html" + '\n'
  x += "delete_key = '@@DELETE@@'  # Delimitador do nome do atributo da tabela para a rotina de exclusão" + '\n'
  x += "delete_value = " + delete_value + "  # Nome do atributo da tabela para a rotina de exclusão" + '\n'
  x += "" + '\n'
  s.write(x)

  insert_form_title_list = listaToString("inc", "titulo")
  insert_form_list = listaToString("inc", "atributo")
  insert_form_column_type_list = listaToString("inc", "tipo")

  x = "# 09 - utilizado na geração no formulario de inclusão em html: inclui.html" + '\n'
  x += "insert_form_key = '@@FORM_INSERT@@'  # Delimitador da lista de atributos para inclusão de dados no banco de dados" + '\n'
  x += "insert_form_title_list = " + insert_form_title_list + "  # Lista dos nomes das colunas para inclui.html" + '\n'
  x += "insert_form_list = " + insert_form_list + "  # Lista de atributos para inclui.html" + '\n'
  x += "insert_form_column_type_list = " + insert_form_column_type_list + "  # Lista dos tipos das colunas para a definição do formulario (forms.py)" + '\n'
  x += "" + '\n'
  s.write(x)

  update_form_title_list = listaToString("alt", "titulo")
  update_form_list = listaToString("alt", "atributo")
  update_form_column_type_list = listaToString("alt", "tipo")

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

  print("GeraCrud", "Arquivo <" + nome_arquivo + "> gerado com sucesso!")


def carregarParams(nome_arquivo):

  try:
    f = open(nome_arquivo, "r")
  except Exception as e:
    return None

  l = list([[],[]])

  for x in f:
    k = ''
    v = ''
    if len(x.split()) > 0 and x.split()[0] != '#': # exclui linhas com espaços ou linhas de comentários(iniciada com '#)'
      k = x.split()[0]
      v = re.findall(r"'(.*?)'", x)
      if len(v) > 0:
        if len(v) == 1:
          l.append([k, v[0]])
        else:
          l.append([k, v])

  for i in range(len(l)):
    p = l[i]
    if len(p) > 0:

      if p[0] == 'table_model_value':
        table_model_value = p[1]

      if p[0] == 'database_name_value':
        database_name_value = p[1]

      if p[0] == 'table_name_value':
        table_name_value = p[1]

      if p[0] == 'table_pk_value':
        table_pk_value = p[1]

      if p[0] == 'table_column_list':
        table_column_list = p[1]

      if p[0] == 'table_column_length_list':
        table_column_length_list = p[1]

      if p[0] == 'table_column_type_list':
        table_column_type_list = p[1]

      if p[0] == 'table_column_type_list':
        table_column_type_list = p[1]

      if p[0] == 'table_column_title_list':
        table_column_title_list = p[1]

      if p[0] == 'search_title_column_list':
        search_title_column_list = p[1]

      if p[0] == 'search_detail_column_list':
        search_detail_column_list = p[1]

      if p[0] == 'search_length_column_list':
        search_length_column_list = p[1]

      if p[0] == 'print_length_column_list':
        print_length_column_list = p[1]

      if p[0] == 'delete_value':
        delete_value = p[1]

      if p[0] == 'insert_form_title_list':
        insert_form_title_list = p[1].copy()

      if p[0] == 'insert_form_list':
        insert_form_list = p[1]

      if p[0] == 'insert_form_column_type_list':
        insert_form_column_type_list = p[1]

      if p[0] == 'update_form_title_list':
        update_form_title_list = p[1].copy()

      if p[0] == 'update_form_list':
        update_form_list = p[1]

      if p[0] == 'update_form_column_type_list':
        update_form_column_type_list = p[1]

  # dados['conexao_bd'] =  conexao_bd # Atualmente não fica arquivado no arquivo
  dados['nome_bd'] =  database_name_value
  dados['nome_tabela'] =  table_name_value
  dados['nome_model'] =  table_model_value

  lista.clear()

  for i in range(len(table_column_list)):

    search_title_column_list_string = listaToString3(search_title_column_list)
    insert_form_title_list_string = listaToString3(insert_form_title_list)
    update_form_title_list_string = listaToString3(update_form_title_list)
    delete_value_string = listaToString4(delete_value, table_column_list)
    table_pk_value_string = listaToString4(table_pk_value, table_column_list)

    new_list = {
      # 'key' : '',
      'atributo': table_column_list[i],
      'pk': table_pk_value_string[i],
      'lis': search_title_column_list_string[i],
      'inc': insert_form_title_list_string[i],
      'alt': update_form_title_list_string[i],
      'exc': delete_value_string[i],
      'tipo': table_column_type_list[i],
      'titulo': table_column_title_list[i],
      'tam_bd': table_column_length_list[i],
      'tam_lista': search_length_column_list[i],
      'tam_relat': print_length_column_list[i]
    }

    lista[i] = new_list


def criticaDados():

  message = None

  conexao_bd = request.form['conexao_bd']
  nome_bd = request.form['nome_bd']
  nome_tabela = request.form['nome_tabela']
  nome_model = request.form['nome_model']

  # if not conexao_bd:
  #   message = "Conexão com BD deve ser preenchido!"
  if not nome_bd:
    message = "Nome do BD deve ser preenchido!"
  elif not nome_tabela:
    message = "Nome da tabela do BD deve ser preenchido!"
  elif not nome_model:
    message = "Nome da tabela do BD no Model deve ser preenchido!"

  return message


def criticaAtributos():

  message = None

  atributo = request.form['atributo']
  titulo = request.form['titulo']
  tam_bd = request.form['tam_bd']
  tam_lista = request.form['tam_lista']
  tam_relat = request.form['tam_relat']

  if not atributo:
    message = "Nome do atributo da tabela do BD deve ser preenchido!"
  elif not titulo:
    message = "Nome Titulo deve ser preenchido!"
  elif not tam_bd:
    message = "Tamanho do atributo no BD deve ser preenchido!"
  elif not tam_lista:
    message = "Tamanho do atributo na Lista de Consulta deve ser preenchido!"
  elif not tam_relat:
    message = "Tamanho do atributo na Lista do Relatório deve ser preenchido!"

  return message


def listaToString(key1, key2):
  i = 0
  lista_string = "["
  for key, value in lista.items():
    i += 1
    if i == len(lista.items()):
      if value.get(key1) == 'T':
        lista_string += "'" + value.get(key2) + "'"
      else:
        lista_string += "''"
    else:
      if value.get(key1) == 'T':
        lista_string += "'" + value.get(key2) + "', "
      else:
        lista_string += "'', "
  lista_string += "]"

  return lista_string


def listaToString1(key1):
  i = 0
  lista_string = "["
  for key, value in lista.items():
    i += 1
    if i == len(lista):
      lista_string += "'" + value.get(key1) + "'"
    else:
      lista_string += "'" + value.get(key1) + "', "
  lista_string += "]"
  return lista_string


def listaToString2(key1, key2):
  for key, value in lista.items():
    if value.get(key1) == 'T':
      lista_string = "'" + value.get(key2) + "'"
      break
  return lista_string


def listaToString3(key1):
  lista_string = ""
  for valor in key1:
    if valor == '':
      lista_string += "F"
    else:
      lista_string += "T"
  return lista_string


def listaToString4(key1, key2):
  lista_string = ""
  for key in key2:
    if key == key1:
      lista_string += "T"
    else:
      lista_string += "F"
  return lista_string


def gerarCrud(nome_arquivo):

  try:
    geracrud.le_parametros(nome_arquivo)
    geracrud.cria_pastas()
    geracrud.gera_lista_html()
    geracrud.gera_inclui_html()
    geracrud.gera_altera_html()
    geracrud.gera_routes()
    geracrud.gera_forms()
    geracrud.gera_models()
    geracrud.cria_tabela()
    message = "CRUD gerado com sucesso!"
  except Exception as e:
    message = "Falha na geração do CRUD do Projeto!"

  lista_sorted = {k : lista[k] for k in sorted(lista.keys())}
  return render_template("index.html", dados=dados, lista=lista_sorted, nova_lista=nova_lista, error=message)


if __name__ == '__main__':
  app.run(debug=True)

