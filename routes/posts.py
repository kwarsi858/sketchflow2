from flask import Flask, jsonify, Blueprint, request
from scripts.db import DB

post_bp = Blueprint('posts', __name__, template_folder ='templates' )


@post_bp.route('/post',methods=['POST'])
def addPost():
    try:
        user_post_data = request.json
        post_collection = DB('posts')
        post_collection.save(user_post_data)
        resp = {'msg':'user post found','payload':user_post_data}
    except Exception as e:
        resp = {'msg':'unable to find user post','error':e}
        
    return jsonify({'resp':resp})

'''
@post_bp.route('/post',methods=['GET'])
def getPost():
    email = request.args.get('email')
    message = request.args.get('message')
    photo = request.args.get('photo')
'''
