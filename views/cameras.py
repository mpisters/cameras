import json

from flask import Blueprint

camera_api = Blueprint('camera_api', __name__)


@camera_api.route("/camera")
def get_cameras():
    return json.dumps([])
