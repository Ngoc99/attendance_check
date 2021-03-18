''' File này chứa các hàm dùng chung bởi các api
'''
import datetime
import json
from flask import jsonify
import sys




def gen_response(response_code=500, message=None, data=None):
    ''' Tạo response

    :Args:
    - response_code 
    - message 

    :Rets:
    - cấu trúc JSON-like - xem chi tiết trong README.md
    '''

    if response_code == 200: 
        return jsonify({
            "response_code" : 200,
            "message" : "Successful" if not message else message,
            "data" : data,
        })
        
    if response_code == 405:
        return jsonify({
            "response_code" : 405,
            "message" : "Invalid format" if not message else message,
            'data' : None,  
            "parameters" : None
        })
    return jsonify({
        "response_code" : 500,
        "message" : "Internal error" if not message else message,
        'data' : None,
        "parameters" : None
    })



def errFileWriter(errContent: str):
    """Ghi lỗi vào file `errors.txt`

    Arguments:
        errContent {str} -- Nội dung traceback bị lỗi
    """

    with open("errors.txt", "a+") as f:
        f.write("\n")
        json.dump(
            {
                "error": errContent,
                "datetime": str(datetime.datetime.now())
            },
            f,
            indent=4
        )
