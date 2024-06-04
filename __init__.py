from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route("/contact/")
def MaPremiereAPI():
    return render_template("contact.html")

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')

@app.route('/somme/<int:val_user>/<int:val_user2>')
def somme(val_user, val_user2):
resultat = val_user + val_user2
if resultat % 2 == 0:
message = "pair"
else:
message = "impair"
return message

if __name__ == "__main__":
  app.run(debug=True)
