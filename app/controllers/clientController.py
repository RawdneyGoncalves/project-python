from flask import Blueprint, jsonify, request
from testeController import generate_fake_data
from conexao import db

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/users', methods=['GET'])
def get_users():
    users = db.users.find()
    return jsonify([user for user in users])

@user_controller.route('/users', methods=['POST'])
def create_user():
    data = generate_fake_data()
    db.users.insert_one(data)
    return jsonify(data), 201

@user_controller.route('/users/<string:user_id>', methods=['GET'])
def get_user(user_id):
    user = db.users.find_one({'_id': user_id})
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user)

@user_controller.route('/users/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    name = data['name']
    result = db.users.update_one({'_id': user_id}, {'$set': {'name': name}})
    if result.modified_count == 0:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'message': 'User updated successfully'})

@user_controller.route('/users/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = db.users.delete_one({'_id': user_id})
    if result.deleted_count == 0:
        return jsonify({'error': 'User not found'}), 404
    return '', 204
