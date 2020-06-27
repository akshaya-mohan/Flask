from flask_jwt import jwt_required
import sqlite3
from flask_restful import Resource,reqparse
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',type=float,required=True,help='Field Empty !')
    parser.add_argument('store_id',type=int,required=True,help='Store id empty !')

    def get(self,name):
        item = ItemModel.find_by_name(name)

        if item:
            return item,200
        return {'message':'Item not found'},404

    @jwt_required()
    def post(self,name):
        if ItemModel.find_by_name(name):
            return {'message':'Item already exists'},400

        data = Item.parser.parse_args()
        item = ItemModel(name,**data) #**data -> data['price'],data['store_id']
        try:
            item.save_to_db()
        except:
            return {'message':'error occured while inserting'}

        return item.json(),201

    @jwt_required()
    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message' : 'Item deleted'}
        
        return {'message':'Item not found'},404

    @jwt_required()
    def put(self,name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name,**data)
        else:
            item['price'] = data['price']
            item['store_id'] = data['store_id']

        item.save_to_db()
        return item.json()
            

class Items(Resource):
    def get(self ):
        return {'items':[i.json() for i in ItemModel.query.all()]}
        
