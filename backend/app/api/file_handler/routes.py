from flask import jsonify, request, Blueprint, abort, current_app
import os
import pyexcel as pe
from app.utils_pkg import gen_response, errFileWriter

###################################################
# FILE Blue Print Definition
file_bp = Blueprint('file_bp', __name__)
###################################################

###################################################
# Upload Excel File from Frontend =>>>>> Backend
###################################################
@file_bp.route("/file_upload", methods=['POST'])
def process_file():
    try: 
        if request.method != "POST": 
            return gen_response(response_code = 405, method = "POST !!! not GET")
    
        # Getting request
        my_file = request.files['name']
        file_name = request.files['name'].filename
        file_ext = os.path.splitext(file_name)[1]

        if (not my_file) or (not file_name): 
            return gen_response(response_code= 405, message = "NO FILE FOUND!")
        if (file_ext not in current_app.config.get('UPLOAD_EXTENSIONS')): 
            return gen_response(response_code = 405, message = "The providedd file is in wrong format! Acceptable format: xls, xlsm, csv")
        
        ##################################################
        # REQUEST HANDLER
        ##################################################
        
        temp_path = ['temp_file', file_ext]
        address = os.path.join("./app/tmp","".join(temp_path))
        print(address)
        my_file.save(address)  
        dataset = pe.get_records(file_name=address)
        my_list = [dict(value) for key, value in enumerate(dataset)]
        print("DB")
        print(current_app)
        return jsonify({"data": my_list,"msg": "successfully uploaded file"}) 
       
    except Exception as e: 
        errFileWriter(traceback.format_exc())
        return gen_response(response_code = 500, message = "Internal Server Error")





