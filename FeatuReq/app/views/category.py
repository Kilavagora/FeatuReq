"""Category Blueprint"""
from flask import Blueprint
from flask import request, jsonify
from app.models.category import Category
from app.errors import bad_request

cat = Blueprint('category', __name__)


@cat.route('/categories/', methods=['GET'])
def get_categories():
    """Get category list"""
    results = [category.to_dict() for category in Category.get_all()]
    return jsonify(results), 200


@cat.route('/categories/', methods=['POST'])
def create_category():
    """Create a category"""
    name = request.json.get("name", '')
    if not name:
        return bad_request(405)
    category = Category(name=name)
    category.save()
    return jsonify(category.to_dict()), 201


@cat.route('/categories/<int:id>', methods=['GET'])
def get_category(id):
    """Get the category by id"""
    category = Category.query.get(id)
    if not category:
        return bad_request(404)
    return jsonify(category.to_dict()), 200


@cat.route('/categories/<int:id>', methods=['PUT'])
def update_category(id):
    """Update the category by id"""
    category = Category.query.get(id)
    if not category:
        return bad_request(404)
    name = request.json.get("name", '')
    if not name:
        return bad_request(405)
    category.name = name
    category.save()
    return jsonify(category.to_dict()), 200


@cat.route('/categories/<int:id>', methods=['DELETE'])
def delete_category(id):
    """Delete the category by id"""
    category = Category.query.get(id)
    if not category:
        return bad_request(404)
    category.delete()
    return jsonify({
        "message": "Category {} has been deleted successfully.".format(category.id)
    }), 200
