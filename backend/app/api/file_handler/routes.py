from flask import jsonify, request, Blueprint
file_bp = Blueprint('file_bp', __name__)
import pandas as pd

#####################################
# Process File and Redirect to Board
#####################################
@file_bp.route("/file_upload", methods=['POST'])
def process_file():
    try: 
        print("abc")
        print(request.files['name'].read())
        print(123)
        print("Dataset =>>>>>")
        const uploaded_file = request.file['name'].read()
        const df = pd.read_csv(uploaded_file.stream)
        print(df.head())

        # if (request.files): 
        #     file_upload = request.data
        #     print(file_upload)
        
        return jsonify({"msg": "successfully uploaded file"})
    # print(file_upload)
    except Exception as e: 
        print(e)
        error = {"error": e, "msg": "fail"}
        return jsonify(error)





