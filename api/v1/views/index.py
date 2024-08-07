#!/usr/bin/python3
"""
create a file index.py
"""

from flask import jsonify
from api.v1.views import app_views
from models import storage

@app_views.route('/status', methods=['GET'])
def get_status():
    stats = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonify({"status": "OK"})

