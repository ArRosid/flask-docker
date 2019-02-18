from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello world 123'

    @app.route('/about')
    def about():
        return 'About'

    return app