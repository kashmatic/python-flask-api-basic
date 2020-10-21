from . import db, ma

class Player(db.Model):
    __tablename__ = 'players'

    uuid = db.Column(db.String(60), primary_key=True)
    name = db.Column(db.String(60), index=True)
    team = db.Column(db.String(60), index=True)

    def __repr__(self):
        return f'<Player name:{self.name} team:{self.team}>'

class PlayerSchema(ma.Schema):
    class Meta:
        model = Player
        fields = ('uuid', 'name', 'team')
