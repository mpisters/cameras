import json

from flask import Blueprint

from modules.cameras import parse_csv_cameras_to_json

camera_api = Blueprint('camera_api', __name__)


@camera_api.route("/api/camera/")
def get_cameras():
    cameras = parse_csv_cameras_to_json('server/data/cameras-defb.csv')
    return json.dumps(cameras)
