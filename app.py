# user_service.py

from flask import Flask, jsonify, request
import requests
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
users = {
        '1': {'name': 'Alice', 'email': 'alice@example.com'},
        '2': {'name': 'Bob', 'email': 'bob@example.com'}
    }
@app.route('/')
def home():
    return "user service is live!"


@app.route('/user/<id>')
def user(id):
    user_info = users.get(id, {})
    return jsonify(user_info)

@app.route('/user/<id>', methods=['GET'])
def read_user(id):
    return jsonify(users.get(id, {}))

@app.route('/user', methods=['POST'])
def create_user():
    data = request.json
    new_id = str(len(users)+1)
    users[new_id] = data
    return jsonify({'message': 'POSTed new user'})

@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
    if id in users:
        user = users[id]
        user['name'] = request.json.get('name', user['name'])
        user['email'] = request.json.get('email', user['email'])
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    if id in users:
        del users[id]
        return jsonify({}), 204
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(port=5000)