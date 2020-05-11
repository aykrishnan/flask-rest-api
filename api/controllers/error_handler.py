from flask import Blueprint, jsonify, request, Response

from api.exceptions import ResourceNotFoundError


error_handler = Blueprint('error_handler', __name__)

@error_handler.app_errorhandler(ResourceNotFoundError)
def handle_resource_not_found(e):
    return jsonify({'error': 'Resource not found', 'message': str(e)}), 404
