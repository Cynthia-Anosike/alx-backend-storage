from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = \
        'mysql://root:''@localhost/record'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = \
        False
db = SQLAlchemy(app)
migrate = Migrate(app, db)



from app import routes
