from flask_restful import Resource, reqparse


class Visual(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('oni',
                            type=int,
                            required=True,)
        parser.add_argument('station', type=int, required=True)
        parser.add_argument('season', type=int, required=True)
        data = parser.parse_args()
        oni = data['oni']
        season = data['season']
        station = data['station']
        print(oni, station, season)
        return {'Message': 'Request was received'}, 200

    @classmethod
    def render_to(cls):
        return 'vis.html'
