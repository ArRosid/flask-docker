from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True

    @app.route('/')
    def index():
        return render_template('index.html', title='Flask 01 - Home')

    @app.route('/about')
    def about():
        return render_template('about.html', title='Flask 01 - About')

    return app