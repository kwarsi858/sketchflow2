from flask import Flask, jsonify, Blueprint, request
from scripts.db import DB

post_bp = Blueprint('posts', __name__, template_folder ='templates' )


@post_bp.route('/post',methods=['POST'])
def addPost():
    user_post_data = request.json
    try:
        post_collection = DB('posts')
        post_collection.save(user_post_data)
        resp = {'msg':'user post found','payload':user_post_data}
    except Exception as e:
        resp = {'msg':'user post not found','error':e}
        
    return jsonify({'resp':resp})


@post_bp.route('/post',methods=['GET'])
def getPost():
    email = request.args.get('email')
    message = request.args.get('message')
    photo = request.args.get('photo')
    getData = DB('posts')
    

