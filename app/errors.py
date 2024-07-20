from flask import Blueprint,jsonify

errors = Blueprint('errors',__name__)
@errors.app_errorhandler(404)
def not_found_error(error):
    return jsonify({'error':'resource not found'}),404

@errors.app_errorhandler(400)
def bad_request_error(error):
    return jsonify({'error':'bad request'}),400

@errors.app_errorhandler(500)
def internal_error(error):
    return jsonify({'error':'Internal Error'}),500