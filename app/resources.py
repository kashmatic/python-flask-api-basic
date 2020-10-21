import uuid

from flask_restful import Resource, reqparse

from . import db
from .models import Player, PlayerSchema

post_parser = reqparse.RequestParser(bundle_errors=True)
post_parser.add_argument('name', type=str, required=True, location='args', help='Required: name')
post_parser.add_argument('team', type=str, required=True, location='args', help='Required: team')

uuid_parser = reqparse.RequestParser(bundle_errors=True)
uuid_parser.add_argument('uuid', type=str, required=True, location='args', help='Required: uuid')
uuid_parser.add_argument('name', type=str, required=False, location='args', help='Required: name')
uuid_parser.add_argument('team', type=str, required=False, location='args', help='Required: team')


class PlayerAllResource(Resource):
    def get(self):
        players = Player.query.order_by('name').all()
        print(players)
        jobj = PlayerSchema(many=True).dump(players)
        return jobj, 200

class PlayerResource(Resource):
    def get(self):
        args = uuid_parser.parse_args()
        player_exists = Player.query.filter_by(uuid=args.uuid).first()
        if not player_exists:
            return {'ERROR': 'No record'}, 409
        result = PlayerSchema().dump(player_exists)
        return result, 200

    def put(self):
        args = uuid_parser.parse_args()
        player_exists = Player.query.filter_by(uuid=args.uuid).first()
        if not player_exists:
            return {'ERROR': 'No record'}, 409
        player_exists.name = args.name
        player_exists.team = args.team
        try:
            db.session.add(player_exists)
            db.session.commit()
        except Exception as e:
            return {'ERROR': str(e)}, 409

        result = PlayerSchema().dump(player_exists)
        return result, 202

    def post(self):
        args = post_parser.parse_args()
        player_exists = Player.query.filter_by(name=args.name, team=args.team).first()
        if player_exists:
            return {'ERROR': 'Duplicate record'}, 409
        player = Player(uuid=str(uuid.uuid4()), name=args.name, team=args.team)
        try:
            db.session.add(player)
            db.session.commit()
        except Exception as e:
            return {'ERROR': str(e)}, 409

        result = PlayerSchema().dump(player)
        return result, 201

    def delete(self):
        args = uuid_parser.parse_args()
        player_exists = Player.query.filter_by(uuid=args.uuid).first()
        if not player_exists:
            return {'ERROR': 'No record'}, 409
        try:
            db.session.delete(player_exists)
            db.session.commit()
        except Exception as e:
            return {'ERROR': str(e)}, 409
        return None, 204
