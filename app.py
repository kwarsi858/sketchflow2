from flask import Flask, Blueprint
from routes.users import user_bp
from routes.posts import post_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(user_bp)
app.register_blueprint(post_bp)

#Pokemon 2000

if __name__ == "__main__":
    app.run(debug=True)