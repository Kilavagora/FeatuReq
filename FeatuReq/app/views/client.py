"""Client Blueprint"""
from flask import Blueprint
from flask import request, jsonify
from app.models.client import Client
from app.errors import bad_request

cli = Blueprint('client', __name__)


@cli.route('/clients/', methods=['GET'])
def get_clients():
    """Get client list"""
    results = [client.to_dict() for client in Client.get_all()]
    return jsonify(results), 200


@cli.route('/clients/', methods=['POST'])
def create_client():
    """Create a client"""
    name = request.json.get("name", '')
    if not name:
        return bad_request(405)
    client = Client(name=name)
    client.save()
    return jsonify(client.to_dict()), 201


@cli.route('/clients/<int:id>', methods=['GET'])
def get_client(id):
    """Get the client by id"""
    client = Client.query.get(id)
    if not client:
        return bad_request(404)
    return jsonify(client.to_dict()), 200


@cli.route('/clients/<int:id>', methods=['PUT'])
def update_client(id):
    """Update the client by id"""
    client = Client.query.get(id)
    if not client:
        return bad_request(404)
    name = request.json.get("name", '')
    if not name:
        return bad_request(405)
    client.name = name
    client.save()
    return jsonify(client.to_dict()), 200


@cli.route('/clients/<int:id>', methods=['DELETE'])
def delete_client(id):
    """Delete the client by id"""
    client = Client.query.get(id)
    if not client:
        return bad_request(404)
    client.delete()
    return jsonify({
        "message": "Client {} has been deleted successfully.".format(client.id)
    }), 200
