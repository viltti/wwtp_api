from flask import Flask
from config import Config
from api import api_bp
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(api_bp, url_prefix="/api")

    return app

app = create_app()

if __name__ == "__main__":
    app = create_app()
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
    
    '''
    if os.getenv('FLASK_ENV') == 'development':
        app.run(debug=True)
    else:
        app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
    '''