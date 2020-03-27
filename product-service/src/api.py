from flask import Flask
from flask_restful import Resource, Api
from typing import List, Dict
import mysql.connector
import json

app = Flask(__name__)

api = Api(app)

def favorite_colors() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'knights'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM favorite_colors')
    results = [{name: color} for (name, color) in cursor]
    cursor.close()
    connection.close()

    return results

class Product(Resource):
	def get(self):
	    return json.dumps({'favorite_colors': favorite_colors()})

api.add_resource(Product,'/')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=3001, debug=True)
