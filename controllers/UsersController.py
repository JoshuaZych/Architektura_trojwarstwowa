from flask import Flask, request, jsonify, abort # type: ignore

from services.UserService import UserService

app = Flask(__name__)
user_service = UserService()


@app.route('/users', methods=['GET'])
def get_users():
    users = user_service.get_all_users()
    return jsonify(users), 200


@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = user_service.get_user_by_id(id)
    if user is None:
        abort(404)
    return jsonify(user), 200


@app.route('/users', methods=['POST'])
def create_user():
    if not request.json or not all(key in request.json for key in ['firstName', 'lastName', 'age', 'group']):
        abort(400)
    user = request.json
    new_user = user_service.create_user(user)
    return jsonify(new_user), 201


@app.route('/users/<int:id>', methods=['PATCH'])
def update_user(id):
    if not request.json:
        abort(400)
    user = user_service.update_user(id, request.json)
    if user is None:
        abort(404)
    return jsonify(user), 200


@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    success = user_service.delete_user(id)
    if not success:
        abort(404)
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
