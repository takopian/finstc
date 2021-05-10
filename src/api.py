from flask import Flask
from flask_restful import Api
from flask_resources.car import Car
from flask_resources.dealer import Dealer
from flask_resources.dealer_to_car import DealerToCar


class App:
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)

    def run(self, *args, **kwargs):

        # Uncomment next lines to initialize database

        # with sqlite3.connect('database.db') as conn:
        #     cursor = conn.cursor()
        #     sql_file = open("schema.sql")
        #     sql_as_string = sql_file.read()
        #     sql_file.close()
        #     cursor.executescript(sql_as_string)
        self.api.add_resource(Car, "/car/<int:car_id>", "/car/add")
        self.api.add_resource(Dealer, "/dealer/<int:dealer_id>", "/dealer/add")
        self.api.add_resource(DealerToCar, "/dealer/<int:dealer_id>/car/<int:car_id>")
        self.app.run(*args, **kwargs)


if __name__ == "__main__":
    app = App()
    app.run(debug=True)

