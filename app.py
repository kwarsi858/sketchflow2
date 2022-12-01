from flask import Flask, Blueprint
from routes.users import user_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(user_bp)

if __name__ == "__main__":
    app.run(debug=True)