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
    emailResp = ''
    passwordResp = ''
    users_Collection = users('registration')
    email = request.args.get("email")
    password = request.args.get("password")
    User = users_Collection.find_one()
    idDelete = del User['_id']
    emailInfo = User['email']
    passwordInfo = User['password']
    if email == emailInfo:
        return {emailResp:emailInfo}
    elif password == passwordInfo:
        return {passwordResp:passwordInfo}
    
    return jsonify({'email':emailresp, 'password':passwordResp})


















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
    
