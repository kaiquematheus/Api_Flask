from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


hoteis = [
	{
		'hotel_id': 'alpha',
		'nome':'Alhpa Hotel',
		'estrelas':4.3,
		'diaria':420.34,
		'cidade':'Rio de Janeiro'
	},
	{
		'hotel_id': 'bravo',
		'nome':'Bravo Hotel',
		'estrelas':4.4,
		'diaria':380.90,
		'cidade':'Santa Catarina'
	},
	{
		'hotel_id': 'charlie',
		'nome':'Charlie Hotel',
		'estrelas':4.5,
		'diaria':450.90,
		'cidade':'São Paulo'
	}
]

class Hoteis(Resource):

	def get(self):
		return {'hoteis': hoteis}

api.add_resource(Hoteis, '/hoteis')

if __name__ == '__main__':
	app.run(debug=True)
	
# http://127.0.0.1:5000/hoteis
