"""Feature Blueprint"""
from datetime import datetime
from flask import Blueprint
from flask import request, jsonify
from app.models.feature import Feature
from app.errors import bad_request

feat = Blueprint('feat', __name__)


@feat.route('/features/', methods=['GET'])
def get_features():
    """GET all /features/"""
    category_id = request.args.get('category', None)
    client_id = request.args.get('client', None)
    completed = request.args.get('completed', False)

    results = []

    if category_id and client_id:
        results = [feature.to_dict() for feature in
                   Feature.query.filter((Feature.category == category_id) &
                                        (Feature.client == client_id) &
                                        (Feature.complete == completed))
                                .order_by(Feature.priority.desc(),
                                          Feature.date_created.desc())
                                .all()]
    elif category_id:
        results = [feature.to_dict() for feature in
                   Feature.query.filter((Feature.category == category_id) &
                                        (Feature.complete == completed))
                                .order_by(Feature.client,
                                          Feature.priority.desc(),
                                          Feature.date_created.desc())
                                .all()]
    elif client_id:
        results = [feature.to_dict() for feature in
                   Feature.query.filter((Feature.client == client_id) &
                                        (Feature.complete == completed))
                                .order_by(Feature.priority.desc(),
                                          Feature.date_created.desc())
                                .all()]
    else:
        results = [feature.to_dict() for feature in
                   Feature.query.filter(Feature.complete == completed)
                                .order_by(Feature.client,
                                          Feature.priority.desc(),
                                          Feature.date_created.desc())
                                .all()]

    response = jsonify(results)
    return response, 200


@feat.route('/features/', methods=['POST'])
def create_feature():
    """Create a feature"""
    feature_dict = request.get_json(silent=True)
    if not feature_dict:
        return bad_request(405)
    try:
        target_date = datetime.strptime(feature_dict.get(
            'target_date', '')[0:10], "%Y-%m-%d")
        feature_dict['target_date'] = target_date
        feature = Feature(**feature_dict)
    except:
        print("Error has occured.")
    else:
        feature.save()
        return jsonify(feature.to_dict()), 201
    return bad_request(405)


@feat.route('/features/<int:id>', methods=['GET'])
def get_feature(id):
    """Get the feature by id"""
    feature = Feature.query.get(id)
    if not feature:
        return bad_request(404)
    return jsonify(feature.to_dict()), 200


@feat.route('/features/<int:id>', methods=['PUT'])
def update_feature(id):
    """Update the feature by id"""
    feature = Feature.query.get(id)  # filter_by(Feature.id=id).first()
    if not feature:
        return bad_request(404)
    try:
        feature_dict = request.get_json(silent=True)
        target_date = datetime.strptime(feature_dict.get(
            'target_date', '')[0:10], "%Y-%m-%d")
        feature_dict['target_date'] = target_date
        feature.__init__(**feature_dict)
        feature.save()
    except:
        print("Cannot update the feature_dict")
    else:
        return jsonify(feature.to_dict()), 200
    return bad_request(405)


@feat.route('/features/<int:id>', methods=['DELETE'])
def delete_feature(id):
    """Delete the feature by id"""
    feature = Feature.query.get(id)  # filter_by(Feature.id=id).first()
    if not feature:
        return bad_request(404)
    feature.delete()
    return jsonify({
        "message": "Feature {} has been deleted successfully."
                   .format(feature.id)
    }), 200
