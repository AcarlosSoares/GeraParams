# Gerador de documentos HTML para tabelas com relacionamento One-To-NoOne
# Criado por Antonio Carlos
# Data: Jul/2019
# coding: utf8
import os
import shutil
import re

# utilizado na geração das rotinas do routes.py
route_list_form_key = '@@LIST_FORM@@'  # Delimitador do nome do form para o formulario de listagem
route_list_form_value = 'ListaForm' # Nome do form para o formulario de listagem
route_insert_form_key = '@@INSERT_FORM@@'  # Delimitador do nome do form para o formulario de inclusão
route_insert_form_value = 'IncluiForm' # Nome do form para o formulario de inclusão
route_update_form_key = '@@UPDATE_FORM@@'  # Delimitador do form para o formulario de alteração
route_update_form_value = 'AlteraForm' # Nome do form para o formulario de alteração

# utilizado na geração das rotinas do routes.py
table_model_key = '@@TABLE_MODEL@@'  # Delimitador do nome da tabela no modelo
table_model_value = 'Client' # Nome da tabela no modelo 'models.py'

# utilizado na geração das rotinas: lista.html, inclui.html, altera.html e routes.py
database_name_key = '@@DATABASE_NAME@@'  # Delimitador do nome da tabela no banco de dados
database_name_value = 'db_ticket' # Nome do schema do banco de dados

# utilizado na geração das rotinas: lista.html, inclui.html, altera.html e routes.py
table_name_key = '@@TABLE_NAME@@'  # Delimitador do nome da tabela no banco de dados
table_name_value = 'client' # Nome da tabela no banco de dados

# utilizado na geração das rotinas do routes.py
table_pk_key = '@@TABLE_PK@@'  # Delimitador do nome da Primary Key da tabela no banco de dados
table_pk_value = 'tenantid' # Nome da Primary Key da tabela no BD

# utilizado na criação do banco de dados
table_column_key = '@@TABLE_COLUMN@@'  # Delimitador do nome das colunas da tabela no banco de dados
table_column_list = ['tenantid', 'description', 'name']  # Nome dos atributos do BD
table_column_type_list = ['int', 'string', 'string']  # Lista dos tipos das colunas do BD - tipos disponiveis: int, string, datetime, text, boolean
table_column_title_list = ['Seq', 'Descrição', 'Nome']  # Nome dos atributos do BD
table_column_length_list = ['10', '255', '255']  # Lista dos tamanhos das colunas do BD

# utilizado na geração no formulario de listagem em html: lista.html
search_title_column_key = '@@TITLE_COLUMN@@'  # Delimitador do nome dos títulos das colunas para a tela: lista.html
search_title_column_list = ['Seq', 'Descrição', 'Nome']  # Lista dos nomes das colunas e labels
search_detail_column_list = ['tenantid', 'description', 'name']  # Nome dos atributos para a criação do banco de dados para a tela: lista.html
search_length_column_list = ['10', '200', '350']  # Lista dos tamanhos das colunas para a tela: lista.html
print_length_column_list = ['30', '150', '300']  # Lista dos tamanhos das colunas para o relatório

# utilizado na geração no formulario de listagem em html: lista.html
delete_key = '@@DELETE@@'  # Delimitador do nome do atributo da tabela para a rotina de exclusão
delete_value = 'name' # Nome do atributo da tabela para a rotina de exclusão

# utilizado na geração no formulario de inclusão em html: inclui.html
insert_form_key = '@@FORM_INSERT@@'  # Delimitador da lista de atributos para inclusão de dados no banco de dados
insert_form_title_list = ['Descrição', 'Nome']  # Lista dos nomes das colunas para inclui.html
insert_form_list = ['description', 'name']   # Lista de atributos para inclui.html
insert_form_column_type_list = ['string', 'string']  # Lista dos tipos das colunas para a definição do formulario (forms.py)

# utilizado na geração no formulario de alteração em html: altera.html
update_form_key = '@@FORM_UPDATE@@'  # Delimitador da lista de atributos para atualização de dados no banco de dados
update_form_title_list = ['Descrição', 'Nome']  # Lista dos nomes das colunas para altera.html
update_form_list = ['description', 'name']   # Lista de atributos para altera.html
update_form_column_type_list = ['string', 'string']  # Lista dos tipos das colunas para a definição do formulario (forms.py)

# utilizado na geração das rotinas do routes.py
insert_sql_key = '@@INSERT_SQL@@'  # Delimitador para montar os campos do insert no banco de dados da função inserir
update_sql_get_key = '@@UPDATE_SQL_GET@@'  # Delimitador para montar os campos do update do metodo GET da função alterar
update_sql_post_key = '@@UPDATE_SQL_POST@@'  # Delimitador para montar os campos do update do metodo POST da função alterar
print_list_key = '@@PRINT_LIST@@'  # Delimitador para montar os campos do relatório
ordenarpor_choices_key = '@@ORDENARPOR_CHOICES@@'  # Delimitador para montar o ordenarpor_choices do forms.py
models_attributes_key = '@@MODELS_ATTR@@'  # Delimitador para montar a lista de atributos do model.py


# pasta = os.getcwd() + '/' + table_name_value + '/'
pasta = os.getcwd() + '/'

def le_parametros(nome_arquivo):

  # print('le_parametros: ' + pasta)

  f = open(nome_arquivo, "r")
  l = list([[],[]])

  for x in f:
    k = ''
    v = ''
    if len(x.split()) > 0:
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

      if p[0] == 'route_list_form_value':
        global route_list_form_value
        route_list_form_value = p[1]

      if p[0] == 'route_insert_form_value':
        global route_insert_form_value
        route_insert_form_value  = p[1]

      if p[0] == 'route_update_form_value':
        global route_update_form_value
        route_update_form_value = p[1]

      if p[0] == 'table_model_value':
        global table_model_value
        table_model_value = p[1]

      if p[0] == 'database_name_value':
        global database_name_value
        database_name_value = p[1]

      if p[0] == 'table_name_value':
        global table_name_value
        table_name_value = p[1]

      if p[0] == 'table_pk_value':
        global table_pk_value
        table_pk_value = p[1]

      if p[0] == 'table_column_list':
        global table_column_list
        table_column_list = p[1]

      if p[0] == 'table_column_length_list':
        global table_column_length_list
        table_column_length_list = p[1]

      if p[0] == 'table_column_type_list':
        global table_column_type_list
        table_column_type_list = p[1]

      if p[0] == 'search_title_column_list':
        global search_title_column_list
        search_title_column_list = p[1].copy()

      if p[0] == 'search_detail_column_list':
        global search_detail_column_list
        search_detail_column_list = p[1]

      if p[0] == 'search_length_column_list':
        global search_length_column_list
        search_length_column_list = p[1]

      if p[0] == 'print_length_column_list':
        global print_length_column_list
        print_length_column_list = p[1]

      if p[0] == 'delete_value':
        global delete_value
        delete_value = p[1]

      if p[0] == 'insert_form_title_list':
        global insert_form_title_list
        insert_form_title_list = p[1].copy()

      if p[0] == 'insert_form_list':
        global insert_form_list
        insert_form_list = p[1]

      if p[0] == 'insert_form_column_type_list':
        global insert_form_column_type_list
        insert_form_column_type_list = p[1]

      if p[0] == 'update_form_title_list':
        global update_form_title_list
        update_form_title_list = p[1].copy()

      if p[0] == 'update_form_list':
        global update_form_list
        update_form_list = p[1]

      if p[0] == 'update_form_column_type_list':
        global update_form_column_type_list
        update_form_column_type_list = p[1]


def cria_pastas():

  path = os.getcwd()

  pasta_projeto = path + '/' + table_name_value
  pasta_template = pasta_projeto + '/templates'

  # print('cria_pastas: ' + pasta_projeto)

  if os.path.exists(pasta_template):
    try:
        shutil.rmtree(pasta_template)  # exclui a pasta e o conteúdo da pasta
        print ("Pasta excluídas com sucesso: %s" % pasta_template)
    except:
        print ("Falha na exclusão da pasta: %s " % pasta_template)

  if os.path.exists(pasta_projeto):
    try:
        shutil.rmtree(pasta_projeto)  # exclui a pasta e o conteúdo da pasta
        print ("Pasta excluídas com sucesso: %s" % pasta_projeto)
    except:
        print ("Falha na exclusão da pasta: %s " % pasta_projeto)

  if not os.path.exists(pasta_projeto):
    try:
        os.mkdir(pasta_projeto)
        print ("Pasta criada com sucesso: %s" % pasta_projeto)
    except:
        print ("Falha na criação da pasta: %s" % pasta_projeto)

  if not os.path.exists(pasta_projeto + '/templates'):
    try:
        os.mkdir(pasta_projeto + '/templates')
        print ("Pasta criada com sucesso: %s" % pasta_template)
    except:
        print ("Falha na criação da pasta: %s" % pasta_template)


def gera_lista_html():

  pasta_template = pasta + table_name_value + '/templates/' + table_name_value + "_lista.html"
  pasta_modelos = pasta + 'modelos/'

  # print('gera_lista_html: ' + pasta_modelos)

  s = open(pasta_template,"w", encoding='utf-8')
  f = open(pasta_modelos + "modelo_lista.html", "r", encoding='utf-8')

  for x in f:

    if table_name_key in x:
      x = x.replace(table_name_key, table_name_value)

    # Título das colunas da lista
    if search_title_column_key in x:
      i = 0
      l = ''
      for c in search_title_column_list:
        if i == 0:
          l += '<th class="text-center" style="width: ' + search_length_column_list[i] + 'px">' + search_title_column_list[i].title() + '</th>' + '\n'
        elif i == len(search_title_column_list) - 1:
          l += ' ' * 16 + '<th class="text-center" style="width: ' + search_length_column_list[i] + 'px">' + search_title_column_list[i].title() + '</th>'
        else:
          l += ' ' * 16 + '<th class="text-center" style="width: ' + search_length_column_list[i] + 'px">' + search_title_column_list[i].title() + '</th>' + '\n'
        i += 1
      x = x.replace(search_title_column_key, l)

    # Detalhe das colunas da lista
    if table_column_key in x:
      i = 0
      l = ''
      for c in search_detail_column_list:
        if i == 0:
          l += '<td>{{ dado.' + search_detail_column_list[i] + ' }}</td>' + '\n'
        elif i == len(search_title_column_list) - 1:
          l += ' ' * 18 + '<td>{{ dado.' + search_detail_column_list[i] + ' }}</td>'
        else:
          l += ' ' * 18 + '<td>{{ dado.' + search_detail_column_list[i] + ' }}</td>' + '\n'
        i += 1
      x = x.replace(table_column_key, l)

    if delete_key in x:
      x = x.replace(delete_key, delete_value)

    if table_pk_key in x:
      x = x.replace(table_pk_key, table_pk_value)

    s.write(x)

  f.close()
  s.close()

def gera_inclui_html():

  pasta_template = pasta + table_name_value + '/templates/' + table_name_value + "_inclui.html"
  pasta_modelos = pasta + 'modelos/'

  # print('gera_inclui_html: ' + pasta_template)

  s = open(pasta_template,"w", encoding='utf-8')
  f = open(pasta_modelos + "modelo_inclui.html", "r", encoding='utf-8')

  for x in f:

    if table_name_key in x:
      x = x.replace(table_name_key, table_name_value)

    if insert_form_key in x:
      i = 0
      l = ''
      for c in insert_form_list:
        if i == 0:
          l += '{{ render_field(form.' + insert_form_list[i] + ') }}' + '\n'
        elif i == len(insert_form_list) - 1:
          l += ' ' * 16 + '{{ render_field(form.' + insert_form_list[i] + ') }}'
        else:
          l += ' ' * 16 + '{{ render_field(form.' + insert_form_list[i] + ') }}' + '\n'
        i += 1
      x = x.replace(insert_form_key, l)

    s.write(x)

  f.close()
  s.close()

def gera_altera_html():

  pasta_template = pasta + table_name_value + '/templates/' + table_name_value + "_altera.html"
  pasta_modelos = pasta + 'modelos/'

  # print('gera_altera_html: ' + pasta_template)

  s = open(pasta_template,"w", encoding='utf-8')
  f = open(pasta_modelos + "modelo_altera.html", "r", encoding='utf-8')

  for x in f:

    if table_name_key in x:
      x = x.replace(table_name_key, table_name_value)

    if update_form_key in x:
      i = 0
      l = ''
      for c in update_form_list:
        if i == 0:
          l += '{{ render_field(form.' + update_form_list[i] + ') }}' + '\n'
        elif i == len(update_form_list) - 1:
          l += ' ' * 16 + '{{ render_field(form.' + update_form_list[i] + ') }}'
        else:
          l += ' ' * 16 + '{{ render_field(form.' + update_form_list[i] + ') }}' + '\n'
        i += 1
      x = x.replace(update_form_key, l)

    s.write(x)

  f.close()
  s.close()

def gera_routes():

  pasta_projeto = pasta + table_name_value + "/routes.py"
  pasta_modelos = pasta + 'modelos/'

  # print('gera_routes: ' + pasta_projeto)

  s = open(pasta_projeto,"w", encoding='utf-8')
  f = open(pasta_modelos + "modelo_routes.py", "r", encoding='utf-8')

  for x in f:

    if table_name_key in x:
      x = x.replace(table_name_key, table_name_value)

    if table_model_key in x:
      x = x.replace(table_model_key, table_model_value)

    if table_pk_key in x:
      x = x.replace(table_pk_key, table_pk_value)

    if route_list_form_key in x:
      x = x.replace(route_list_form_key, route_list_form_value)

    if route_insert_form_key in x:
      x = x.replace(route_insert_form_key, route_insert_form_value)

    if route_update_form_key in x:
      x = x.replace(route_update_form_key, route_update_form_value)

    if insert_sql_key in x:
      i = 0
      l = ''
      for c in insert_form_list:
        l += insert_form_list[i] + '=form.' + insert_form_list[i] + '.data'
        i += 1
        if i < len(insert_form_list):
          l += ', '
      x = x.replace(insert_sql_key, l)

    if update_sql_get_key in x:
      i = 0
      l = ''
      for c in update_form_list:
        # trata a primeira ocorrencia
        if i == 0:
          l += 'form.' + update_form_list[i] + '.data = dado.' + update_form_list[i] + '\n'
         # trata a ultima ocorrencia
        elif i == len(update_form_list) - 1:
          l += ' ' * 6 + 'form.' + update_form_list[i] + '.data = dado.' + update_form_list[i]
        # trata as demais ocorrencias
        else:
          l += ' ' * 6 + 'form.' + update_form_list[i] + '.data = dado.' + update_form_list[i]  + '\n'
        i += 1
      x = x.replace(update_sql_get_key, l)

    if update_sql_post_key in x:
      i = 0
      l = ''
      for c in update_form_list:
        # trata a primeira ocorrencia
        if i == 0:
          l += 'dado.' + update_form_list[i] + ' = form.' + update_form_list[i] + '.data' + '\n'
        # trata a ultima ocorrencia
        elif i == len(update_form_list) - 1:
          l += ' ' * 6 + 'dado.' + update_form_list[i] + ' = form.' + update_form_list[i] + '.data'
        # trata as demais ocorrencias
        else:
          l += ' ' * 6 + 'dado.' + update_form_list[i] + ' = form.' + update_form_list[i] + '.data' + '\n'
        i += 1
      x = x.replace(update_sql_post_key, l)

    if print_list_key in x:
      i = 0
      l = ''
      m = 50
      n = 0
      for c in search_title_column_list:
        # trata a primeira ocorrencia
        n = m + int(print_length_column_list[i])
        if i == 0:
          l += '[' + "'" + search_title_column_list[i].title() + "'" + ', ' + "'" + 'row.' + table_column_list[i] + "'"  + ', ' + str(m) + ', ' + str(n) + ']' + ',\n'
        # trata a ultima ocorrencia
        elif i == len(search_title_column_list) - 1:
          l += ' ' * 4 + '[' + "'" + search_title_column_list[i].title() + "'" + ', ' + "'" + 'row.' + table_column_list[i] + "'"  + ', ' + str(m) + ', ' + str(n) + ']'
        # trata as demais ocorrencias
        else:
          l += ' ' * 4 + '[' + "'" + search_title_column_list[i].title() + "'" + ', ' + "'" + 'row.' + table_column_list[i] + "'"  + ', ' + str(m) + ', ' + str(n) + ']' + ',\n'
        m = n + 20
        i += 1
      x = x.replace(print_list_key, l)

    s.write(x)

  f.close()
  s.close()


def gera_forms():

  pasta_projeto = pasta + table_name_value + "/forms.py"
  pasta_modelos = pasta + 'modelos/'

  # print('gera_forms: ' + pasta_projeto)

  s = open(pasta_projeto,"w", encoding='utf-8')
  f = open(pasta_modelos + "modelo_forms.py", "r", encoding='utf-8')

  for x in f:

    if table_name_key in x:
      x = x.replace(table_name_key, table_name_value)

    if table_model_key in x:
      x = x.replace(table_model_key, table_model_value.lower().capitalize())

    if ordenarpor_choices_key in x:
      i = 0
      l = ''
      for c in search_title_column_list:
        if i == 0:
          l += '(' + "'" +  table_name_value + '.' + table_column_list[i] + "'" + ',' + "'" + search_title_column_list[i].title() + "'" + '),'
        elif i == len(search_title_column_list) - 1:
          l += '(' + "'" +  table_name_value + '.' + table_column_list[i] + "'" + ',' + "'" + search_title_column_list[i].title() + "'" + ')'
        else:
          l += '(' + "'" +  table_name_value + '.' + table_column_list[i] + "'" + ',' + "'" + search_title_column_list[i].title() + "'" + '),'
        i += 1
      x = x.replace(ordenarpor_choices_key, l)

    if route_insert_form_key in x:
      i = 0
      l = ''
      for c in insert_form_list:
        # trata a primeira ocorrencia
        if i == 0:
          l += insert_form_list[i] + ' = ' + tipo_atributo_form(insert_form_column_type_list[i]) + '(' + "'" + insert_form_title_list[i] + "'" + ', validators=[DataRequired()])' + '\n'
        # trata a ultima ocorrencia
        elif i == len(insert_form_list) - 1:
          l += ' ' * 2 + insert_form_list[i] + ' = ' + tipo_atributo_form(insert_form_column_type_list[i]) + '(' + "'" + insert_form_title_list[i] + "'" + ', validators=[DataRequired()])'
        # trata as demais ocorrencias
        else:
          l += ' ' * 2 + insert_form_list[i] + ' = ' + tipo_atributo_form(insert_form_column_type_list[i]) + '(' + "'" + insert_form_title_list[i] + "'" + ', validators=[DataRequired()])' + '\n'
        i += 1
      x = x.replace(route_insert_form_key, l)

    if route_update_form_key in x:
      i = 0
      l = ''
      for c in update_form_list:
        # trata a primeira ocorrencia
        if i == 0:
          l += update_form_list[i] + ' = ' + tipo_atributo_form(update_form_column_type_list[i]) + '(' + "'" + update_form_title_list[i] + "'" + ', validators=[DataRequired()])' + '\n'
        # trata a ultima ocorrencia
        elif i == len(update_form_list) - 1:
          l += ' ' * 2 + update_form_list[i] + ' = ' + tipo_atributo_form(update_form_column_type_list[i]) + '(' + "'" + update_form_title_list[i] + "'" + ', validators=[DataRequired()])'
        # trata as demais ocorrencias
        else:
          l += ' ' * 2 + update_form_list[i] + ' = ' + tipo_atributo_form(update_form_column_type_list[i]) + '(' + "'" + update_form_title_list[i] + "'" + ', validators=[DataRequired()])' + '\n'
        i += 1
      x = x.replace(route_update_form_key, l)

    s.write(x)

  f.close()
  s.close()


def gera_models():

  pasta_projeto = pasta + table_name_value + "/models.py"
  pasta_modelos = pasta + 'modelos/'

  # print('gera_models: ' + pasta_projeto)

  s = open(pasta_projeto,"w", encoding='utf-8')
  f = open(pasta_modelos + "modelo_models.py", "r", encoding='utf-8')

  for x in f:

    if table_name_key in x:
      x = x.replace(table_name_key, table_name_value)

    if table_model_key in x:
      x = x.replace(table_model_key, table_model_value)

    if models_attributes_key in x:
      i = 0
      l = ''
      for c in table_column_list:
        # trata a primeira ocorrencia
        if i == 0:
          l += table_column_list[i] + '= db.Column(' + "'" + table_column_list[i] + "'" + ', db.Integer, primary_key=True)' + '\n'
        # trata a ultima ocorrencia
        elif i == len(table_column_list) - 1:
          l += ' ' * 4 + table_column_list[i] + '= db.Column(' + "'" + table_column_list[i] + "'" + ', db.' + tipo_atributo_model(table_column_type_list[i]) + '(' + table_column_length_list[i] + '), nullable=False)'
        # trata as demais ocorrencias
        else:
          l += ' ' * 4 + table_column_list[i] + '= db.Column(' + "'" + table_column_list[i] + "'" + ', db.' + tipo_atributo_model(table_column_type_list[i]) + '(' + table_column_length_list[i] + '), nullable=False)' + '\n'
        i += 1
      x = x.replace(models_attributes_key, l)

    s.write(x)

  f.close()
  s.close()

def cria_tabela():

  pasta_projeto = pasta + table_name_value + "/cria_tabela.py"
  pasta_modelos = pasta + 'modelos/'

  # print('cria_tabela: ' + pasta_projeto)

  s = open(pasta_projeto,"w")
  f = open(pasta_modelos + "modelo_cria_tabela.py", "r")

  for x in f:

    if database_name_key in x:
      x = x.replace(database_name_key, database_name_value)

    if table_name_key in x:
      x = x.replace(table_name_key, table_name_value)

    if table_pk_key in x:
      x = x.replace(table_pk_key, table_pk_value)

    if table_column_key in x:
      i = 0
      l = ''
      for c in table_column_list:
        # trata a primeira ocorrencia
        if i == 0:
          l += table_column_list[i] + ' int(11) NOT NULL AUTO_INCREMENT,' + '\n'
        # trata a ultima ocorrencia
        elif i == len(table_column_list) - 1:
          l += ' ' * 4 + table_column_list[i] + ' ' + tipo_atributo_bd(table_column_type_list[i]) + '(' + table_column_length_list[i] + ') NOT NULL,' + '\n'
          l += ' ' * 4 + 'PRIMARY KEY (' + table_pk_value + ')'
        # trata as demais ocorrencias
        else:
          l += ' ' * 4 + table_column_list[i] + ' ' + tipo_atributo_bd(table_column_type_list[i]) + '(' + table_column_length_list[i] + ') NOT NULL,' + '\n'
        i += 1
      x = x.replace(table_column_key, l)

    s.write(x)

  f.close()
  s.close()

def tipo_atributo_bd(valor):
  if valor == 'string':
    return 'varchar'
  if valor == 'int':
    return 'int'
  if valor == 'datetime':
    return 'datetime'
  if valor == 'text':
    return 'text'
  if valor == 'boolean':
    return 'tinyint'
  else:
    return '?????'

def tipo_atributo_model(valor):
  if valor == 'string':
    return 'String'
  if valor == 'int':
    return 'Integer'
  if valor == 'datetime':
    return 'DateTime'
  if valor == 'text':
    return 'Text'
  if valor == 'boolean':
    return 'Boolean'
  else:
    return '?????'

def tipo_atributo_form(valor):
  if valor == 'string':
    return 'StringField'
  if valor == 'int':
    return 'IntegerField'
  if valor == 'datetime':
    return 'DateField'
  if valor == 'text':
    return 'TextAreaField'
  if valor == 'boolean':
    return 'BooleanField'
  else:
    return '?????'

