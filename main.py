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
def connexion():
	email = request.form.get('email')
	password = request.form.get('password')

	mycursor = mydb.cursor()
	sql = "SELECT * FROM Clients WHERE AdresseEmail = %s"
	val = (email,)
	mycursor.execute(sql, val)
	client = mycursor.fetchone()

	if client:
		hashed_password = client[5].encode('utf-8')
		if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
			return jsonify({'success': True, 'message': 'Connexion réussie'})
		else:
			return jsonify({'success': False, 'message': 'Adresse email ou mot de passe invalide'})
	else:
		return jsonify({'success': False, 'message': 'Adresse email ou mot de passe invalide'})


@app.route("/api/Inscription", methods=['POST'])
def Inscription():
	pass


@app.route("/api/Deconnexion", methods=['POST'])
def Deconnexion():
	pass


@app.route("/api/rechercheProduit", methods=['POST'])
def rechercheProduit():
	# try:
	# 	reponse = make_response(jsonify({"redirect": "/Recherche", "message": request.form}))
	# 	return reponse
	# except:
	# 	return ("", 404)
	pass


@app.route("/Recherche")
def Recherche():
	# params = []
	# mycursor.callproc("selection_produits")
	pass


@app.route("/api/ajouterPanier", methods=['POST'])
def ajouterPanier():
	# try:
	#     produit_id = int(request.form['produit_id'])
	#     user_id = int(request.form['user_id'])
	#     mycursor.execute("INSERT INTO Commandes (ID_Produit, ID_Client) VALUES (%s, %s)", (produit_id, user_id))
	#     mydb.commit()
	#     return make_response(jsonify({'message': 'Produit ajouté au panier'}), 200)
	# except:
	#     return make_response(jsonify({'error': 'Failed to add product to cart'}), 500)
	pass


@app.route("/api/supprimerPanier", methods=['POST'])
def supprimerPanier():
	# try:
	# 	produit_id = int(request.form['produit_id'])
	# 	user_id = int(request.form['user_id'])
	# 	mycursor.execute("DELETE FROM Commandes WHERE ID_Produit = %s AND ID_Client", (produit_id, user_id))
	# 	mydb.commit()
	# 	return make_response(jsonify({'message': 'Produit supprimé du panier'}), 200)
	# except:
	# 	return make_response(jsonify({'error': 'Failed to remove product from cart'}), 500)
	pass


@app.route("/api/commanderPanier", methods=['POST'])
def commanderPanier():
	# try:
	# 	resp = make_response(jsonify({"redirect": "/Commande", "message": request.form}))
	# 	return resp
	# except:
	# 	return ("", 404)
	pass


@app.route("/Commande")
def Commande():
	pass


@app.route("/api/Noter", methods=['POST'])
def Noter():
	pass


if __name__ == "__main__":
	app.run(port=63342)
