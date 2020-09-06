from flask import Flask

from views.cameras import camera_api

app = Flask(__name__)
app.register_blueprint(camera_api)

@app.route('/')
def hello_world():
    return 'Hello World! - Camera API'


if __name__ == '__main__':
    app.run()
