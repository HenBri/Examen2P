from flask_appbuilder import AppBuilder, Model
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(metadata=Model.metadata)
appbuilder = AppBuilder()
