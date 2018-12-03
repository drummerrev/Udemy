from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
	def get(self, name):
		## Could use a for loop for this... but,	
		# for item in items:
		# 	if item['name'] == name:
		# 		return item

		## A better way is to use a filter function with a lambda
		item = next(filter(lambda x: x['name'] == name, items), None)
		# "next" method gives us the next in the list

		return {'item': item}, 200 if item else 404	

	def post(self, name):
		if next(filter(lambda x: x['name'] == name, items), None) is not None:
			return{'message': "An item with name '{}' already exists.".format(name)}, 400


		data = request.get_json()
		item = {'name': name, 'price': data['price']}
		items.append(item)
		return item, 201

class ItemList(Resource):
	def get(self):
		return {'items': items}


api.add_resource(Item, '/item/<string:name>') #http://127.0.0.1:5000/student/Rolf
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)


