from os import environ 
MONGO_URI = environ.get('MONGO_URI')
UPLOAD_EXTENSIONS = environ.get("UPLOAD_EXTENSIONS")