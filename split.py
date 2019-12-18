from flask_restful import Resource


class Split(Resource):
    @classmethod
    def get(cls):
        # 여기에서 로직 처리
        # ...
        # ...

        return {'data': 'hello split'}
