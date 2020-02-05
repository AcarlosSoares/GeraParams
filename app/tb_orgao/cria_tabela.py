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

#   CREATE DATABASE IF NOT EXISTS db_projeto_modelo

#   """)
# db.commit()

#use database
cursor.execute("""

  USE db_projeto_modelo

  """)
db.commit()

#drop table
cursor.execute("""

  DROP TABLE IF EXISTS tb_orgao

  """)

db.commit()

#create table

cursor.execute("""

  CREATE TABLE tb_orgao (

    id_orgao int(11) NOT NULL AUTO_INCREMENT,
    dsc_orgao varchar(60) NOT NULL,
    PRIMARY KEY (id_orgao)

  ) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8;

  """)

db.commit()

cursor.close()
