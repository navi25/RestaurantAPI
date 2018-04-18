from flask import Flask, redirect, render_template
from app import api_bp
from model import db

app = Flask(__name__)

def create_app(config_filename):
    app.config.from_object(config_filename)
    app.register_blueprint(api_bp, url_prefix='/api/v1.0')
    db.init_app(app)
    return app

@app.route('/')
@app.route('/api/')
@app.route('/api/v1.0/')
def availableApps():
    return render_template('availableApp.html')

if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)
