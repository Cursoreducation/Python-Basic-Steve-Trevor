import flask
from flask_restful import Api, Resource, reqparse
from apitest.exceptions import *

app = flask.Flask(__name__)
api = Api(app)


class Register(Resource):
    def get(self, params):
        # parser = reqparse.RequestParser()
        # parser.add_argument("name")
        # parser.add_argument("psw")
        # params = parser.parse_args()
        print("get", params)
        status, code = self.chek_psw(params["psw"])
        if status is False:
            if code == 1:
                raise PswLenError
            if code == 2:
                raise PswWrongSymbolsError
        status, code = self.chek_name(params["psw"])
        if status is False:
            if code == 11:
                raise NameLenError
            if code == 21:
                raise NameWrongSymbolsError

    def chek_psw(self, psw):
        if len(psw) < 6:
            return False, 1

        black_list = ["(", "!"]

        for l in psw:
            if l in black_list:
                return False, 2

    def chek_name(self, name):
        if len(name) < 2:
            return False, 11
        black_list = ["(", "!"]

        for l in name:
            if l in black_list:
                return False, 21


api.add_resource(Register, "/register")

if __name__ == '__main__':
    app.run(debug=True)
