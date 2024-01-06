from flask_restful import Resource, reqparse
from models.hotel_model import HotelModel
from bd.table import insert_bd, get_bd, get_item, update_bd, delete_bd

class Hoteis(Resource):

	def get(self):
          
		return {'hoteis': get_bd()}
	
class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')
    
    def get(self, hotel_id):

        hotel = get_item(hotel_id)
        if hotel:
             return hotel
        return {'message': 'Hotel not found.'}, 404 # not found
	
    def post(self, hotel_id):
        
        dados = Hotel.argumentos.parse_args()

        hotel_objeto = HotelModel(hotel_id, **dados)

        novo_hotel= hotel_objeto.json()

        hotel = insert_bd(**novo_hotel)

        #hoteis.append(novo_hotel)

        return hotel, 200

    def put(self, hotel_id):

        """
        dados = Hotel.argumentos.parse_args()

        hotel_objeto = HotelModel(hotel_id, **dados)

        novo_hotel= hotel_objeto.json()

        hotel = get_item(hotel_id)
        if hotel:
            hotel = update_bd(novo_hotel[1], novo_hotel[2], novo_hotel[3],novo_hotel[4])
            return novo_hotel, 200 # ok
    
        hotel = insert_bd(**novo_hotel)
        return hotel, 201 # criado """
        return {'message':'Implementando!'}

    def delete(self, hotel_id):
        delete_bd(hotel_id)
        
        return {'message':'Hotel deleted'}, 200