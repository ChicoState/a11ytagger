from flask import Flask


def create_app():
    app = Flask(__name__)
    
    @app.route('/')
    def hello_world():
        return 'Hello, World!'
    
    @app.route('/health')
    def health_check():
        return {'status': 'healthy'}, 200
    
    return app


app = create_app()