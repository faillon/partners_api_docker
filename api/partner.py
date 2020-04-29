from flask import Blueprint, Response, request
from models.Partner import Partner
import logging
from bson.json_util import dumps

partners = Blueprint('partners', __name__)

#home for api
@partners.route('/')
def api_home():
    return "Partners RESTful API Home"

#method for retreiving all partners
# @partners.route("/partners", methods=['GET'])
def list_partners():

    logging.info("[list_partners]")

    partners = Partner.objects().to_json()

    if len(list(partners)) == 0:
        Response(dumps({"message": "No partners found."}), mimetype="application/json", status=200) 

    return Response(partners, mimetype="application/json", status=200)


#method for retreive a particular parter by its id
# @partners.route('/partners/<id>', methods=['GET'])
def get_partner(id):

    logging.info("[get_partner]")
    logging.info("Searching for partner with id ["+ str(id)+"]")

    try:
        response = Partner.objects().get(partnerId=id).to_json()
    except Exception as e:
        logging.info(e.args)
        return Response(dumps({"message": e.args}), mimetype="application/json", status=400)
        
    return Response(response, mimetype="application/json", status=200)

#method for create a new partner
# @partners.route('/partners', methods=['POST'])
def create_partner():
    body = request.get_json()

    logging.info("[create_partner]")
    logging.info("Json Received "+ dumps(body))
    
    try:
        partner = Partner(**body).save()
        id = partner.partnerId
    except Exception as e:
        logging.info(e.args)
        return Response(dumps({'message': e.args}), 400)
    
    return Response(dumps({'id': str(id)}), 201)

#method for finding the nearest partner from a given location (latitude, longitude)
# @partners.route('/partners/nearest', methods=['GET'])
def find_nearest_partner():
    logging.info("[find_nearest_partner]")
    
    try:
        latitude = float(request.args.get('latitude',''))
        longitude = float(request.args.get('longitude',''))
        
        logging.info("Searching for partners near ["+str(latitude)+","+str(longitude)+"]")
    except Exception as e:
        return Response(dumps({"message": e.args}), 400)
    
    closest_partner = Partner.find_nearest_partner(latitude, longitude)
    
    logging.info("Closest partner Found")
    logging.info(closest_partner)
    
    return Response(closest_partner, 200)