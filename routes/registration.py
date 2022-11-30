from flask import Flask, request, jsonify, Blueprint
from scripts.db import users

# registered user
user_bp = Blueprint('registration', __name__, template_folder='templates')



@user_bp.route('/user', methods=['POST'])
def newUser():
    users_Collection = users('registration')
    user_data = request.json
    users_Collection.insert_one(user_data)
    return jsonify({'msg':'success'})



@user_bp.route('/user', methods=['GET'])
def getUser():
    users_Collection = users('registration')
    email = request.args.get("email")
    password = request.args.get("password")

    user = users_Collection.find_one({'email':email,'password':password})
    del user['_id']
    return jsonify({'user':user})



@user_bp.route('/user',methods=['PUT'])
def updateUser():
    # retrieve data from db by email identifier
    users_Collection = users('registration')
    email = request.args.get('email')
    getUser = users_Collection.find_one({'email': email})

    # updated data from post form 
    postData = request.json
    if postData['email'] == getUser:
        del getUser['email'] # deleting the original mongodb entry by using email as an identifier. 
        users_Collection.insert_one(postData) # replacing the entry with the updated user collection. 
        resp = 'success'
    else:
        resp = 'none'

    return jsonify({'resp':resp})

@user_bp.route('/user',methods=['DELETE'])
def deleteUser():
    try:
        users_Collection = users('registration')
        email = request.args.get('email')
        getUser = users_Collection.find_one({'email':email})
        del getUser['email']
        resp = {'msg':success}
    except Exception as e: 
        resp = {'error':str(e)}

    return jsonify(resp)

        

  

    return jsonify({'msg'})

















"""

User data model 




1. Users login
    a. email
    b. username
    c. password
    d. post
        d1. images 
        d2. comments

2. Users Registration
    a. firstname
    b. lastname
    c. email
    d. password

3. Posts
    a. message
        a1. image
        a2. comment

"""
    
