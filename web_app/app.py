from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello World'

    @app.route('/about')
    def about():
        return 'About Me'

    return app