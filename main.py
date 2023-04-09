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
def register():
	pass


@app.route("/api/Connexion", methods=['POST'])
def login():
	pass


@app.route("/api/Inscription", methods=['POST'])
def create_account():
	pass


@app.route("/api/Deconnexion", methods=['POST'])
def sign_out():
	pass


@app.route("/api/Recherche", methods=`'POST')
def search():
	pass


@app.route("/api/ajouterPanier", methods=['POST'])
def louerAppartment():
	pass


if __name__ == "__main__":
	app.run(port=3500)
