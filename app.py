from flask import Flask, Blueprint
from routes.registration import user_bp


app = Flask(__name__)
app.register_blueprint(user_bp)


app.run(debug=True)