import sqlite3
from flask_restful import reqparse,Resource
from models.user import UserModel


class Register_user(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',type=str,required=True,help='Field cant be empty')
    parser.add_argument('password',type=str,required=True,help='Field cant be empty')

    def post(self):
        data = Register_user.parser.parse_args()

        if UserModel.find_username(data['username']):
            return {'message':'username already exists'},400

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL,?,?)"
        cursor.execute(query,(data['username'],data['password']))

        connection.commit()
        connection.close()

        return {'message':'User created successfully'},201

        
        


