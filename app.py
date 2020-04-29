from database.mongoengine.db import initialize_db
from flask import Flask, Response
import os
import logging
from api.partner import partners
from dotenv import load_dotenv
import connexion
from flask_cors import CORS


connx_app = connexion.App(__name__, specification_dir='api/')

# Read the api_spec.yaml file to configure the endpoints
connx_app.add_api('api_spec.yaml')

app = connx_app.app

#not very safe but it just needs to add the permited origins
cors = CORS(app, resources={r"*": {"origins": "*"}})

logging.basicConfig(filename='logger.log',level=logging.DEBUG)
logger = logging.getLogger(__name__)

#loads enviroment variblaes from .env file
load_dotenv()

host = os.environ.get('MONGODB_URI')

app.config['MONGODB_SETTINGS'] = {
    'host': host
}

initialize_db(app)
app.register_blueprint(partners)

#to avoid this we could use Apache or Nginx
#but to keet it simple we use this way
if __name__ == '__main__':
    app.run(host='0.0.0.0')