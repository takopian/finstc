from flask_restful import Resource, abort, reqparse
from src.db import DB

car_args = reqparse.RequestParser()
car_args.add_argument("name", type=str, help="Name of the car", required=True)


class Car(Resource):
    def get(self, car_id):
        if not DB.get_car_by_id(car_id):
            return abort(404, message="Could not find car with that id")
        result = DB.get_car_info_by_id(car_id)
        print(result)
        response = {'car_id': car_id, 'dealers': []}
        for res in result:
            response['dealers'].append({'dealer_name': res[0], 'price': res[1], 'quantity': res[2]})
        return response

    def post(self):
        args = car_args.parse_args()
        try:
            result = DB.add_car(args['name'])
            response = {'id': result[0][0], 'name': args['name']}
            return response, 201
        except Exception as e:
            abort(404, message=e.__str__())

    def delete(self, car_id):
        if not DB.get_car_by_id(car_id):
            return abort(404, message="Could not find car with that id")
        try:
            DB.delete_car(car_id)
            return {'success': True}, 200
        except Exception as e:
            abort(404, message=e.__str__())

    def patch(self, car_id):
        args = car_args.parse_args()
        try:
            DB.update_car(car_id, args['name'])
            return {'success': True}, 201
        except Exception as e:
            abort(404, message=e.__str__())

