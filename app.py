from flask import Flask
from flask_restful import Api
from flask_jwt import JWT,jwt_required
from db import db

from resources.item import Item,Items
from resources.user import Register_user
from security import authenticate,identity
from resources.store import Store,StoreList 

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' #tells where data.db is
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.secret_key='asdfghjkl'
api = Api(app)

@app.before_first_request   #runs before the first request
def create_tables():  #All the tables you need SQLAlchemy to create should be imported before this,only then it will create that table
    db.create_all()  #creates data.db 



jwt = JWT(app,authenticate,identity)

api.add_resource(Item,'/item/<string:name>')
api.add_resource(Items,'/items')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')
api.add_resource(Register_user,'/register')

if __name__ == "__main__":
    db.init_app(app)   
    app.run(port=5000,debug=True)

