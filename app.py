from flask import Flask, jsonify
from database import db
from models.user import User
from models.meal import Meal

app = Flask(__name__)

app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3306/daily-diet'

db.init_app(app)

@app.route("/")
def daily_diet():
    return jsonify({"message": "Projeto Daily Diet"})

if __name__ == "__main__":
    app.run(debug=True)