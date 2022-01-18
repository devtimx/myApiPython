from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)

    return app