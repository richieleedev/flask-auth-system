from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

# === Init extensions ===
db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    load_dotenv()

    app = Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///local.db")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")

    db.init_app(app)
    jwt.init_app(app)

    from routes.auth_routes import auth_bp  # ✅ corrected
    app.register_blueprint(auth_bp, url_prefix="/api/auth")

    return app
