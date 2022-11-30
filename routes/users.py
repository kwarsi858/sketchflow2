from flask import Flask, request, jsonify, Blueprint
from scripts.db import connect_to_db

# registered user
user_bp = Blueprint('users', __name__, template_folder='templates')

# Add Try Excepts
# Consistent Payload | Ex. {'data': '', 'msg: '', 'err':''}
# Add better information printing
"""
localhost:5000/user?email=farazfkm@gmail.com GET | Argument
localhost:5000/user/farazfkm@gmail.com PUT | Endpoint
"""

@user_bp.route('/user', methods=['GET'])
def getUser():
    print('Triggering GET /user')

    try:
        users_collection = connect_to_db('users')
        email = request.args.get("email")
        password = request.args.get("password")

        user = users_collection.find_one({'email':email, 'password':password})
        if user:
            print("Found user!")
            del user['_id']
            return jsonify({'user':user})
        else:
            return jsonify({'error': "User not found!"})
    except Exception as e:
        return jsonify({'error':str(e)})

@user_bp.route('/user', methods=['POST'])
def newUser():
    users_collection = connect_to_db('users')
    user_data = request.json
    users_collection.insert_one(user_data)
    return jsonify({'msg': f'Saved User'})

@user_bp.route('/user/<email>',methods=['PUT'])
def updateUser(email):
    try:
        # retrieve data from db by email identifier
        users_collection = connect_to_db('users')

        postData = request.json
        users_collection.update_one({'email': email}, {"$set":postData}) # replacing the entry with the updated user collection. 
        resp = {'msg':f'Updated User {email}'}
    except Exception as e:
        resp = {'msg':'error', 'error':str(e),}  

    return jsonify(resp)

@user_bp.route('/user/<email>', methods=['DELETE'])
def deleteUser(email):
    try:
        users_collection = connect_to_db('users')
        users_collection.delete_one({"email":email})   #deletes the user
        resp = {'msg':f"Deleted User {email}"}
    except Exception as e: 
        resp = {'error':str(e)}

    return jsonify(resp)

        

  

















"""

User data model 




1. Users login
    a. email
    b. username
    c. password
    d. post
        d1. images 
        d2. comments

2. Users users
    a. firstname
    b. lastname
    c. email
    d. password

3. Posts
    a. message
        a1. image
        a2. comment

"""
    
