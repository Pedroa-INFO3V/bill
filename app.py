from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

from utils import conectaBD
from dotenv import load_dotenv

@app.route("/")
def inicio():
    return render_template("form.html")

@app.route("/envioFormulario", methods=["POST"])
def envio():
    n = request.form.get('nome')
    c = request.form.get('cidade')
    dn = request.form.get('nascimento')

    if n =="":
        n =None
    if c =="":
        c = None
    if dn =="":
        dn = None

    cnx = conectaBD()

    cursor = cnx.cursor()
    sql = "INSERT INTO pessoa (nome, cidade, nascimento) VALUES (%s, %s, %s)"
    dados = (n, c, dn)

    cursor.execute(sql, dados)
    cnx.commit()

    cnx.close()

    return render_template('sucesso.html')

@app.route("/remover")
def remover():
    return render_template("formRemover.html")

@app.route("/formRemover")
def formRemover():
    n = request.form.get('nome')
    dados = (n,)
    cnx = conectaBD()
    cursor = cnx.cursor()

    sql = "DELETE from pessoa WHERE nome = %s"

    cursor.execute(sql,dados)
    cnx.commit()

    cnx.close()

    return render_template("sucesso.html")