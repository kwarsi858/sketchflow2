from flask import Flask
from flask import Blueprint


sketchflow_blueprint = Blueprint('route_sketch',__name__)



sketchflow = Flask(__name__)


sketchflow.run(debug = True, port =5000)