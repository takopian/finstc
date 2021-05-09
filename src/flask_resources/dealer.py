from flask_restful import Resource, abort, reqparse
from src.db import DB

dealer_args = reqparse.RequestParser()
dealer_args.add_argument("name", type=str, help="Name of the dealer", required=True)


class Dealer(Resource):

    def get(self, dealer_id):
        if not DB.get_dealer_by_id(dealer_id):
            return abort(404, message="Could not find dealer with that id")
        result = DB.get_dealer_info_by_id(dealer_id)
        response = {'dealer_id': dealer_id, 'cars': []}
        for res in result:
            response['cars'].append({'car_name': res[0], 'price': res[1], 'quantity': res[2]})
        return response

    def post(self):
        args = dealer_args.parse_args()
        try:
            result = DB.add_dealer(args['name'])
            response = {'id': result[0][0], 'name': args['name']}
            return response, 201
        except Exception as e:
            abort(404, message=e.__str__())

    def delete(self, dealer_id):
        if not DB.get_dealer_by_id(dealer_id):
            return abort(404, message="Could not find dealer with that id")
        try:
            DB.delete_dealer(dealer_id)
            return {'success': True}, 200
        except Exception as e:
            abort(404, message=e.__str__())

    def patch(self, dealer_id):
        args = dealer_args.parse_args()
        try:
            DB.update_dealer(dealer_id, args['name'])
            return {'success': True}, 201
        except Exception as e:
            abort(404, message=e.__str__())
