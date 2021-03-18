from flask import jsonify, request, Blueprint

home_bp = Blueprint('home_bp', __name__)

# @home_bp.route('/', methods=['GET','POST'])
# def upload_file(): 
#     if request.method != 'GET': 

#####################################
# TEST CONNECTION
#####################################
@home_bp.route("/")
def home(): 
    return "Hello"

@home_bp.route("/say_hi", methods=['GET'])
def say_hi(): 
    return jsonify({"data": "Back end say hi to front end", "msg": "ADUDU"})
#####################################







