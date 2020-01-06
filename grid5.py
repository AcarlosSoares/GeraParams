# fonte: https://stackoverflow.com/questions/39573035/how-to-delete-entire-row-in-tkinter-grid-layout

from tkinter import *
from tkinter import ttk


i = 7
rows = []
items = []

def add_lista(lista):

    global items

    lista_inv = list(zip(*lista))

    # print(lista_inv)

    for k in range(len(lista_inv)):

        add_row()

        # Atributo da Coluna
        d = Entry(root, width = 35)
        d.delete(0, END)
        d.insert(INSERT, lista_inv[k][0])
        d.grid(row = i, column = 1)

        # Pk
        e = Checkbutton(root)
        e.grid(row = i, column = 2)
        if lista_inv[k][4] == '1':
            e.select()

        # Inc
        e1 = Checkbutton(root)
        e1.grid(row = i, column = 3)
        if lista_inv[k][9] != '':
            e1.select()

        # Alt
        e2 = Checkbutton(root)
        e2.grid(row = i, column = 4)
        if lista_inv[k][10] != '':
            e2.select()

        # Exc
        e3 = Checkbutton(root)
        e3.grid(row = i, column = 5)
        if lista_inv[k][8] == '1':
            e3.select()

        # Tipo da Coluna
        listaValores = ['int','string','datetime','text','boolean']
        f = ttk.Combobox(root, width = 14, values=listaValores)
        f.set(lista_inv[k][1])
        f.grid(row = i, column = 6)

        # Título da Coluna
        g = Entry(root, width=20)
        g.delete(0, END)
        g.insert(INSERT, lista_inv[k][2])
        g.grid(row = i, column = 7)

        # Tamanho da Coluna
        h = Entry(root, width=16)
        h.delete(0, END)
        h.insert(INSERT, lista_inv[k][3])
        h.grid(row = i, column = 8)

        # Tamanho da Lista
        m = Entry(root, width=16)
        m.delete(0, END)
        m.insert(INSERT, lista_inv[k][6])
        m.grid(row = i, column = 9)

        # Tamanho da Lista
        n = Entry(root, width=16)
        n.delete(0, END)
        n.insert(INSERT, lista_inv[k][7])
        n.grid(row = i, column = 10)

def add_row():

    global i
    i = i + 1

    global items

    # Select
    var_c = IntVar()
    c = Checkbutton(root, variable = var_c)
    c.val = var_c
    items.append(c)
    c.grid(row = i, column = 0)

    # Atributo da Coluna
    d = Entry(root, width = 35)
    items.append(d)
    d.grid(row = i, column = 1)

    # Pk
    var_e = IntVar()
    e = Checkbutton(root, variable = var_e)
    items.append(e)
    e.grid(row = i, column = 2)

    # Inc
    var_e1 = IntVar()
    e1 = Checkbutton(root, variable = var_e1)
    items.append(e1)
    e1.grid(row = i, column = 3)

    # Alt
    var_e2 = IntVar()
    e2 = Checkbutton(root, variable = var_e2)
    items.append(e2)
    e2.grid(row = i, column = 4)

    # Exc
    var_e3 = IntVar()
    e3 = Checkbutton(root, variable = var_e3)
    items.append(e3)
    e3.grid(row = i, column = 5)

    # Tipo da Coluna
    var_f = StringVar()
    f = ttk.Combobox(root, width = 14, textvariable = var_f)
    f['values'] = ('int','string','datetime','text','boolean')
    items.append(f)
    f.grid(row = i, column = 6)

    # Título da Coluna
    g = Entry(root, width=20)
    items.append(g)
    g.grid(row = i, column = 7)

    # Tamanho da Coluna
    h = Entry(root, width=16)
    items.append(h)
    h.grid(row = i, column = 8)

    # Tamanho da Coluna da Lista de Consulta
    m = Entry(root, width=16)
    items.append(g)
    m.grid(row = i, column = 9)

    # Tamanho da Coluna do Relatório
    n = Entry(root, width=16)
    items.append(h)
    n.grid(row = i, column = 10)

    rows.append(items)

def delete_row():

    for rowno, row in reversed(list(enumerate(rows))):

        if row[0].val.get() == 1:
            for i in row:
                i.destroy()
            rows.pop(rowno)


def carregarParams():

    f = open("geracrud.cnf", "r", encoding='utf-8')

    global i
    i = 7

    lista = []

    for x in f:

        if 'database_name_value' in x:
            v = re.findall(r"'(.*?)'", x)
            e102 = Entry(root, width = 35)
            e102.delete(0, END)
            e102.insert(INSERT, v[0])
            e102.grid(row=1, column=1)

        if 'table_name_value' in x:
            v = re.findall(r"'(.*?)'", x)
            e103 = Entry(root, width = 35)
            e103.delete(0, END)
            e103.insert(INSERT, v[0])
            e103.grid(row=2, column=1)

        if 'table_model_value' in x:
            v = re.findall(r"'(.*?)'", x)
            e104 = Entry(root, width = 35)
            e104.delete(0, END)
            e104.insert(INSERT, v[0])
            e104.grid(row=3, column=1)

        if 'table_pk_value' in x:
            pk = re.findall(r"'(.*?)'", x)

        if 'delete_value' in x:
            exc = re.findall(r"'(.*?)'", x)

        if 'insert_form_list' in x:
            inc = re.findall(r"'(.*?)'", x)

        if 'update_form_list' in x:
            alt = re.findall(r"'(.*?)'", x)

        if 'table_column_list' in x:
            v = re.findall(r"'(.*?)'", x)
            lista.append(v)

        if 'table_column_type_list' in x:
            v = re.findall(r"'(.*?)'", x)
            lista.append(v)

        if 'table_column_title_list' in x:
            v = re.findall(r"'(.*?)'", x)
            lista.append(v)

        if 'table_column_length_list' in x:
            v = re.findall(r"'(.*?)'", x)
            lista.append(v)

        if 'search_detail_column_list' in x:
            sdcl = re.findall(r"'(.*?)'", x)

        if 'search_length_column_list' in x:
            slcl = re.findall(r"'(.*?)'", x)

        if 'print_length_column_list' in x:
            plcl = re.findall(r"'(.*?)'", x)

    l1 = []
    for k in range(len(lista[0])):
        if k == lista[0].index(pk[0]):
            l1.append('1')
        else:
            l1.append('0')
    lista.append(l1)

    l2 = []
    for k in range(len(lista[0])):
        if lista[0][k] in sdcl:
            l2.append(lista[0][k])
        else:
            l2.append('')
    lista.append(l2)

    l3 = []
    ind = 0
    for k in range(len(lista[0])):
        if lista[0][k] in sdcl:
            l3.append(slcl[ind])
            ind += 1
        else:
            l3.append('')
    lista.append(l3)

    l4 = []
    ind = 0
    for k in range(len(lista[0])):
        if lista[0][k] in sdcl:
            l4.append(plcl[ind])
            ind += 1
        else:
            l4.append('')
    lista.append(l4)

    l5 = []
    for k in range(len(lista[0])):
        if k == lista[0].index(exc[0]):
            l5.append('1')
        else:
            l5.append('0')
    lista.append(l5)

    l6 = []
    ind = 0
    for k in range(len(lista[0])):
        if lista[0][k] in inc:
            l6.append(inc[ind])
            ind += 1
        else:
            l6.append('')
    lista.append(l6)

    l7 = []
    ind = 0
    for k in range(len(lista[0])):
        if lista[0][k] in alt:
            l7.append(alt[ind])
            ind += 1
        else:
            l7.append('')
    lista.append(l7)

    # print(lista)
    # print()

    add_lista(lista)

    f.close()


def gerarParams(self):
    pass


root = Tk()
fonte = ("Verdana", "12")

lb1 = ttk.Label(root, text="Conexão com BD:", font=fonte, width=20).grid(row=0, column=0)
e101 = Entry(root, width = 35).grid(row=0, column=1)

lb2 = ttk.Label(root, text="Nome do BD:", font=fonte, width=20).grid(row=1, column=0)
e102 = Entry(root, width = 35).grid(row=1, column=1)

lb3 = ttk.Label(root, text="Nome da Tabela:", font=fonte, width=20).grid(row=2, column=0)
e103 = Entry(root, width = 35).grid(row=2, column=1)

lb4 = ttk.Label(root, text="Nome da Tabela Model:", font=fonte, width=20).grid(row=3, column=0)
e104 = Entry(root, width = 35).grid(row=3, column=1)

row1 = 6
bt = ttk.Button(root, text='Carregar Params', command=carregarParams).grid(row=row1, column=6)
dl = ttk.Button(root, text='Gerar Params', command=gerarParams).grid(row=row1, column=7)
bt = ttk.Button(root, text='Adicionar Linha', command=add_row).grid(row=row1, column=9)
dl = ttk.Button(root, text='Excluir Linha', command=delete_row).grid(row=row1, column=10)

row2 = 7
v0 = StringVar()
v0.set('Select')
e0 = Entry(root, width=5, font=fonte, textvariable=v0, state='readonly').grid(row=row2, column=0)

v1 = StringVar()
v1.set('Atributo')
e1 = Entry(root, width=21, font=fonte, textvariable=v1, state='readonly').grid(row=row2, column=1)

v2 = StringVar()
v2.set('Pk')
e2 = Entry(root, width=3, font=fonte, textvariable=v2, state='readonly').grid(row=row2, column=2)

v21 = StringVar()
v21.set('Inc')
e21 = Entry(root, width=3, font=fonte, textvariable=v21, state='readonly').grid(row=row2, column=3)

v22 = StringVar()
v22.set('Alt')
e22 = Entry(root, width=3, font=fonte, textvariable=v22, state='readonly').grid(row=row2, column=4)

v23 = StringVar()
v23.set('Exc')
e23 = Entry(root, width=3, font=fonte, textvariable=v23, state='readonly').grid(row=row2, column=5)

v3 = StringVar()
v3.set('Tipo')
e3 = Entry(root, width=10, font=fonte, textvariable=v3, state='readonly').grid(row=row2, column=6)

v4 = StringVar()
v4.set('Titulo')
e4 = Entry(root, width=12, font=fonte, textvariable=v4, state='readonly').grid(row=row2, column=7)

v5 = StringVar()
v5.set('Tam. BD')
e5 = Entry(root, width=10, font=fonte, textvariable=v5, state='readonly').grid(row=row2, column=8)

v6 = StringVar()
v6.set('Tam. Lista')
e6 = Entry(root, width=10, font=fonte, textvariable=v6, state='readonly').grid(row=row2, column=9)

v7 = StringVar()
v7.set('Tam. Relat')
e7 = Entry(root, width=10, font=fonte, textvariable=v7, state='readonly').grid(row=row2, column=10)


mainloop()
