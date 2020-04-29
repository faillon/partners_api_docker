from database.mongoengine.db import db
from bson.json_util import dumps

class Partner(db.Document):
    _id = db.ObjectIdField()
    partnerId = db.IntField(db_field='id')
    tradingName = db.StringField(required=True)
    ownerName = db.StringField(required=True)
    document = db.StringField(required=True, unique=True)
    coverageArea = db.MultiPolygonField(required=True)
    address = db.PointField(required=True)

    @staticmethod
    def find_nearest_partner(latitude, longitude):

        pipeline = [
            {
                "$geoNear": {
                    "near": { "type": "Point", "coordinates": [longitude, latitude ] },
                    "distanceField": "calcDistance"
                }
            },
            { "$limit" : 1 }
        ]

        return  dumps(Partner.objects().aggregate(pipeline))