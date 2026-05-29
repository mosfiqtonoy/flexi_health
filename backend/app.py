from flask import Flask
from routes.auth import auth
from routes.wallet import wallet
from routes.blood import blood
from routes.doctor import doctor
from routes.emergency import emergency

app = Flask(__name__)

app.register_blueprint(auth)
app.register_blueprint(wallet)
app.register_blueprint(blood)
app.register_blueprint(doctor)
app.register_blueprint(emergency)

@app.route("/")
def home():
    return {"message": "Flexi Health API Running"}

if __name__ == "__main__":
    app.run(debug=True)cribe your problem")
