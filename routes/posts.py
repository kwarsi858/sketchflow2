from flask import Flask, jsonify, Blueprint, request
from scripts.db import DB
import uuid

post_bp = Blueprint('posts', __name__, template_folder ='templates' )

@post_bp.route('/post',methods=['GET'])
def getPost():
    try:
        email = request.args.get('email')
        message = request.args.get('message')
        photo = request.args.get('photo')
        collection = DB('posts')
        post = collection.get({'email':email,'message':message,'photo':photo}) # This is a wall feed post

        if post:
            del post['_id']
            resp = {'post':post,'msg':'success'}
        else:
            resp = {'msg':'', 'error':'post not found'}

    except Exception as e:
        print(str(e))
        resp = {'msg':resp,'error':str(e)}

    return jsonify(resp)

@post_bp.route('/post',methods=['POST'])
def newPost():
    user_post_data = request.json
    try:
        collection = DB('posts')
        newID = uuid.uuid4().hex
        user_post_data['id'] = newID
        collection.save(user_post_data)

        msg = 'post saved'
        error = ''
    except Exception as e:
        print(str(e))
        msg = ''
        error = str(e)

    return jsonify({'data':'','msg':msg,'error':error})

@post_bp.route('/post/<id>',methods=['PUT'])
def updatePost(id):
    try:
        postData = request.json
        collection = DB('posts')
        isUpdated = collection.update({'id':id}, {'$set' : postData})
        print(isUpdated)
        if not isUpdated:
            msg = 'failed to update'
            error = ''
        else:
            msg = 'post updated'
            error = ''
    except Exception as e:
        print(str(e))
        msg = ''
        error = str(e)

    return jsonify({'data':'','msg':msg,'error':error})

@post_bp.route('/post/<id>',methods=['DELETE'])
def deletePost(id):
    try:
        collection = DB('posts')
        collection.delete({'id':id})
        msg = 'post deleted'
        error = ''
    except Exception as e:
        print(str(e))
        msg = ''
        error = str(e)

    return jsonify({'msg':msg,'error':error})











    
