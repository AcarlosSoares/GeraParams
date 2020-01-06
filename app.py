# fonte: https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956

from usuarios import Usuarios
from tkinter import *
from tkinter import messagebox

class Application:

    def __init__(self, master=None):

        self.fonte = ("Verdana", "12")

        self.container_titulo = Frame(master)
        self.container_titulo["padx"] = 5
        self.container_titulo["pady"] = 5
        self.container_titulo.pack()

        self.container_conexaoBD = Frame(master)
        self.container_conexaoBD["padx"] = 5
        self.container_conexaoBD["pady"] = 5
        self.container_conexaoBD.pack()

        self.container_nomeBD = Frame(master)
        self.container_nomeBD["padx"] = 5
        self.container_nomeBD["pady"] = 5
        self.container_nomeBD.pack()

        self.container_nomeTabela = Frame(master)
        self.container_nomeTabela["padx"] = 20
        self.container_nomeTabela["pady"] = 5
        self.container_nomeTabela.pack()

        self.container_nomeTabelaModel = Frame(master)
        self.container_nomeTabelaModel["padx"] = 20
        self.container_nomeTabelaModel["pady"] = 5
        self.container_nomeTabelaModel.pack()

        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()

        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()

        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()

        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        self.lbl_titulo = Label(self.container_titulo, text="Gerador de Parâmentros - Python GeraCrud")
        self.lbl_titulo["font"] = ("Calibri", "14", "bold")
        self.lbl_titulo.pack ()

        self.lbl_conexaoBD = Label(self.container_conexaoBD, text="Conexão com BD:", font=self.fonte, width=20)
        self.lbl_conexaoBD.pack(side=LEFT)

        self.txt_conexaoBD = Entry(self.container_conexaoBD)
        self.txt_conexaoBD["width"] = 25
        self.txt_conexaoBD["font"] = self.fonte
        self.txt_conexaoBD.pack(side=LEFT)

        self.lbl_nomeBD = Label(self.container_nomeBD, text="Nome do BD:", font=self.fonte, width=20)
        self.lbl_nomeBD.pack(side=LEFT)

        self.txt_nomeBD = Entry(self.container_nomeBD)
        self.txt_nomeBD["width"] = 25
        self.txt_nomeBD["font"] = self.fonte
        self.txt_nomeBD.pack(side=LEFT)

        self.lbl_nomeTabela = Label(self.container_nomeTabela, text="Nome da Tabela:", font=self.fonte, width=20)
        self.lbl_nomeTabela.pack(side=LEFT)

        self.txt_nomeTabela = Entry(self.container_nomeTabela)
        self.txt_nomeTabela["width"] = 25
        self.txt_nomeTabela["font"] = self.fonte
        self.txt_nomeTabela.pack(side=LEFT)

        self.lbl_nomeTabelaModel = Label(self.container_nomeTabelaModel, text="Nome da Tabela Model:", font=self.fonte, width=20)
        self.lbl_nomeTabelaModel.pack(side=LEFT)

        self.txt_nomeTabelaModel = Entry(self.container_nomeTabelaModel)
        self.txt_nomeTabelaModel["width"] = 25
        self.txt_nomeTabelaModel["font"] = self.fonte
        self.txt_nomeTabelaModel.pack(side=LEFT)

        self.bntCarregar = Button(self.container8, text="Carregar", font=self.fonte, width=12)
        self.bntCarregar["command"] = self.carregarParams
        self.bntCarregar.pack(side=LEFT)

        self.bntGerar = Button(self.container8, text="Gerar", font=self.fonte, width=12)
        self.bntGerar["command"] = self.gerarParams
        self.bntGerar.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()


    def carregarParams(self):
        f = open("geracrud.cnf", "r", encoding='utf-8')

        for x in f:

            if 'database_name_value' in x:
                v = re.findall(r"'(.*?)'", x)
                self.txt_nomeBD.delete(0, END)
                self.txt_nomeBD.insert(INSERT, v[0])

            if 'table_name_value' in x:
                v = re.findall(r"'(.*?)'", x)
                self.txt_nomeTabela.delete(0, END)
                self.txt_nomeTabela.insert(INSERT, v[0])

            if 'table_model_value' in x:
                v = re.findall(r"'(.*?)'", x)
                self.txt_nomeTabelaModel.delete(0, END)
                self.txt_nomeTabelaModel.insert(INSERT, v[0])

        f.close()


    def gerarParams(self):
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
        x += "table_model_value = '" + self.txt_nomeTabelaModel.get() + "'" + '\n'
        s.write(x)

        x = "database_name_key = '@@DATABASE_NAME@@'" + '\n'
        x += "database_name_value = '" + self.txt_nomeBD.get() + "'" + '\n'
        s.write(x)

        x = "table_name_key = '@@TABLE_NAME@@'" + '\n'
        x += "table_name_value = '" + self.txt_nomeTabela.get() + "'" + '\n'
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

        messagebox.showinfo("GeraCrud", "Arquivo <geragrud.cnf> gerado com sucesso!")


root = Tk()
# root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())
root.geometry("600x400")
root.title("Account Login") # set the title of GUI window
root.configure(background="Gray")
Application(root)
root.mainloop()
