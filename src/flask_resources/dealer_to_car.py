from flask_restful import Resource, abort, reqparse
from db import DB

dealer_to_car_args = reqparse.RequestParser()
dealer_to_car_args.add_argument("quantity", type=int, help="Quantity of cars", required=True)
dealer_to_car_args.add_argument("price", type=int, help="Price of car", required=True)

dealer_to_car_patch_args = reqparse.RequestParser()
dealer_to_car_patch_args.add_argument("quantity", type=int, help="Quantity of cars")
dealer_to_car_patch_args.add_argument("price", type=int, help="Price of car")


class DealerToCar(Resource):
    def get(self, dealer_id, car_id):
        result = DB.get_dealer_car_info(dealer_id, car_id)
        if not result:
            return abort(404, message="Could not find info")
        print(result)
        response = {'dealer_id': dealer_id, 'car': {'car_name': result[0], 'price': result[1], 'quantity': result[2]}}
        return response

    def post(self, dealer_id, car_id):
        args = dealer_to_car_args.parse_args()
        try:
            DB.add_dealer_car_info(dealer_id, car_id, args['quantity'], args['price'])
            return {'success': True}, 200
        except Exception as e:
            abort(404, message=e.__str__())

    def delete(self, dealer_id, car_id):
        try:
            DB.delete_dealer_car_info(dealer_id, car_id)
            return {'success': True}, 200
        except Exception as e:
            abort(404, message=e.__str__())

    def patch(self, dealer_id, car_id):
        args = dealer_to_car_patch_args.parse_args()
        try:
            DB.update_dealer_car_info(dealer_id, car_id, args.get('quantity'), args.get('price'))
            return {'success': True}, 200
        except Exception as e:
            abort(404, message=e.__str__())
