#!/usr/bin/python3
"""
 create a file __init__.py
"""

from flask import Blueprint
from api.v1.views.index import *

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
