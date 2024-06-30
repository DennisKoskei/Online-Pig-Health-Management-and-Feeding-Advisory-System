from flask import Flask, current_app, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Pig, HealthRecord, FeedRecord, Disease
from routes import initialize_routes
from database.config import Config


app = Flask(__name__)
app.config.from_object(Config)

# Initialize SQLAlcchemy
db.init_app(app)

# Create tables (only once during application initialization)
with app.app_context():
        db.create_all()

initialize_routes(app)

@app.route('/')
def index():
    return 'Hello, World! Forever'

if __name__ == '__main__':
    app.run(debug=True)