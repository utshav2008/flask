from flask_restplus import Namespace, Resource

api = Namespace('application1', description='App2')


@api.route("/endpoint1")
class Class1(Resource):

    def get(self):
        # any function
        return result


@api.route("/endpoint2")
class Class2(Resource):

    def get(self):
        # any function()
        return result
