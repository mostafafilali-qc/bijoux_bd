import os
import bcrypt
import jwt
# from flask_cors import CORS
import pymysql
from dotenv import load_dotenv
from flask import Flask, jsonify, make_response, request, render_template

load_dotenv()
app = Flask(__name__)
mydb = pymysql.connect(
	host="localhost",
	user=os.getenv('DBPUSER'),
	password=os.getenv('DBPASSWORD'),
	database="bijoux"
)
mycursor = mydb.cursor()


@app.route("/")
def Accueil():
	pass


@app.route("/api/Connexion", methods=['POST'])
def Connexion():
	pass


@app.route("/api/Inscription", methods=['POST'])
def Inscription():
	pass


@app.route("/api/Deconnexion", methods=['POST'])
def Deconnexion():
	pass


@app.route("/api/rechercheProduit", methods=['POST'])
def rechercheProduit():
	pass


@app.route("/api/recherche")
def Recherche():
	pass


@app.route("/api/ajouterPanier", methods=['POST'])
def ajouterPanier():
	pass


@app.route("/api/suprimmerPanier", methods=['POST'])
def suprimmerPanier():
	pass


@app.route("/api/commanderPanier", methods=['POST'])
def commanderPanier():
	pass


@app.route("/api/Commande", methods=['POST'])
def Commande():
	pass


@app.route("/api/Noter", methods=['POST'])
def Noter():
	pass


if __name__ == "__main__":
	app.run(port=3500)
