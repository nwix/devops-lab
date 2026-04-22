from flask import Flask 
app = Flask(__name__) 

@app.route("/") 
def home():
    # Pour la Partie 7, changez ce texte par "Version 2 Déployée automatiquement" [cite: 161, 162]
    return "Version 2 CI/CD avec Jenkins" 

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000) 