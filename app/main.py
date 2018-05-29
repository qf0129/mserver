from flask import Flask
from app.config import configs

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(configs[config_name])

    @app.route('/')
    def index():
        from flask import current_app
        return 'hello ' + current_app.config['TEXT']

    return app

