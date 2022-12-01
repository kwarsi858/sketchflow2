from flask import Flask, jsonify, Blueprint
from scripts.db import DB

post_bp = Blueprint('posts', __name__, template_folder ='templates' )
