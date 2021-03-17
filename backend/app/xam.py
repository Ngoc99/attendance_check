# @app.route('/')
# def flask_mongodb_atlas():
#     return "<h1>Hello World!</h1><p>"+str(user_collection)+"</p>"

# @app.route('/users', methods=['POST'])
# def create_users(): 
#     # print(request.json)
#     new_user = user_collection.insert({
#         'name': request.json['name'], 
#         'email': request.json['email'],
#         'password': request.json['password'],
#     })
#     return jsonify(str(ObjectId(new_user)))

# @app.route('/users', methods=['GET'])
# def get_users():
#     users = []
#     for u in user_collection.find():
#         users.append({
#             '_id': str(ObjectId(u['_id'])),
#             'name': u['name'],
#             'email':u['email'],
#             'password':u['password'],
#         })
        
#     return jsonify(users)

# @app.route('/users/<id>', methods=['GET'])
# def get_a_user(id): 
#     u = user_collection.find_one({"_id": ObjectId(id)})
#     return jsonify({
#         "_id": str(ObjectId(u['_id'])), 
#         "name": u['name'], 
#         "email": u['email'], 
#         "password": u['password'], 

#     })

# @app.route('/users/<id>', methods=['DELETE'])
# def delete_a_user(id): 
#     u = user_collection.find_one_and_delete({"_id": ObjectId(id)})
#     return jsonify({"msg": "User Deleted"})

# @app.route('/users/<id>', methods=['PUT'])
# def update_a_user(id): 
#     u = user_collection.find_one_and_update({
#         "_id": ObjectId(id), 
#         "$set":{
#             'name': request.json['name'], 
#             'email': request.json['email'], 
#             'password': request.json['password']
#         }
#     })
#     return jsonify({'msg': 'User\'s Updated'})