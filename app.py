from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS

from split import Split

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')

api.add_resource(Split, '/split')

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')
