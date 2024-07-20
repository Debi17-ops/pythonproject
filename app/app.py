
from flask import Flask
from config import Config
from models import db
from flask_sqlalchemy import SQLAlchemy

# Initializing the flask application
app = Flask(__name__)

# Specifying a default welcome message
@app.route('/')
def welcome():
    return "Welcome to the Employee Management System"


# Setting up with the config file
app.config.from_object(Config)

# Iniitalizing the app
db.init_app(app)

with app.app_context():
    db.create_all()

from routes import *

#app.register_blueprint(main_blueprint)

from errors import errors as errors_blueprint
app.register_blueprint(errors_blueprint)

# Running the application
if __name__ == "__main__":
    app.run(debug=True)