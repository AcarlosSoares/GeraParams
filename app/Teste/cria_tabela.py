# import mysql.connector as conn  # instalar: mysql-connector-python-8.0.16-py3.7-windows-x86-32bit.msi
import pymysql  # pipenv install pymysql

#connect to server: mysql-connector-python-8.0.16-py3.7-windows-x86-32bit.msi
# db=conn.connect(host="localhost", user="root", password="admin")

#connect to server: pymysql
# db = pymysql.connect("localhost", "root", "admin", "db_projeto_modelo" )
db = pymysql.connect("localhost", "root", "admin" )

cursor=db.cursor()

#create database
# cursor.execute("""

#   CREATE DATABASE IF NOT EXISTS Teste

#   """)
# db.commit()

#use database
cursor.execute("""

  USE Teste

  """)
db.commit()

#drop table
cursor.execute("""

  DROP TABLE IF EXISTS Teste

  """)

db.commit()

#create table

cursor.execute("""

  CREATE TABLE Teste (

    id_empresa int(11) NOT NULL AUTO_INCREMENT,
    ds_nomefantasia_emp varchar(10) NOT NULL,
    ds_razaosocial_emp varchar(10) NOT NULL,
    ds_cnpj_emp varchar(10) NOT NULL,
    ds_cidade_emp varchar(10) NOT NULL,
    PRIMARY KEY (id_empresa)

  ) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8;

  """)

db.commit()

cursor.close()
