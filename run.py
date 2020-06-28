from app import app
from db import db

db.init_app(app)

@app.before_first_request   #runs before the first request
def create_tables():  #All the tables you need SQLAlchemy to create should be imported before this,only then it will create that table
    db.create_all()  #creates data.db 