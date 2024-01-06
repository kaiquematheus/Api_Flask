from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel

app = Flask(__name__)
# Configuração do banco de dados
DB_NAME = 'banco.db'
api = Api(app)


api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')

if __name__ == '__main__':
	from bd.table import create_table
	create_table() # Cria a tabela
	app.run(debug=True)
	
# http://127.0.0.1:5000/hoteis
