from flask import Flask, redirect, render_template
from app import api_bp
from model import db
from config import DevelopmentConfig, TestingConfig

app = Flask(__name__)

t = 0
def create_app(config_filename):
    app.config.from_object(config_filename)
    global t
    if t == 0:
        app.register_blueprint(api_bp, url_prefix='/api/v1.0')
        t = 1
    if config_filename != TestingConfig:
        print("config is not Testing confid so initiating db here")
        db.init_app(app)
    return app

@app.route('/')
@app.route('/api/')
@app.route('/api/v1.0/')
def availableApps():
    return render_template('availableApp.html')


if __name__ == "__main__":
    app = create_app(DevelopmentConfig)
    app.run(debug=True)
