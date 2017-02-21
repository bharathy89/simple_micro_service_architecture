from flask import Flask, jsonify, request, abort
import grpc
import os
import json
import logging
import sys
import user_pb2
import user_pb2_grpc
from protobuf_to_dict import protobuf_to_dict

logger = logging.getLogger('myapp')
hdlr = logging.FileHandler('./app/myapp.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.WARNING)

app = Flask(__name__)

context = ('./app/cert.crt', './app/key.key')

@app.route("/")
def hello():
  return "Hello world!"

@app.route("/users", methods=['GET'])
def get_users():
  user_list = user_pb2.User_list()
  val = stub.GetUsers(user_list)
  val = protobuf_to_dict(val)
  return jsonify(val)

@app.route("/users/<string:name>", methods=['GET'])
def get_user(name):
  user_name = user_pb2.User_Name(Name=name)
  val= stub.GetUser(user_name)
  val = protobuf_to_dict(val)
  if val:
    return jsonify(val)
  else:
    abort(404)

@app.route("/users/<string:name>", methods=['DELETE'])
def delete_user(name):
  user_name = user_pb2.User_Name(Name=name)
  val= stub.DeleteUser(user_name)
  val = protobuf_to_dict(val)
  if val:
    return jsonify(val)
  else:
    abort(404)

@app.route("/users", methods=["POST"])
def add_users():
  if not request.json or not 'Name' in request.json or \
    not 'Occupation' in request.json:
    abort(400)
  value = request.json
  print("request json"+ str(value))
  logger.info("request json : "+str(request.json))
  user = user_pb2.User(Name=value["Name"], Occupation=value["Occupation"], Hobbies=value["Hobbies"])
  response = stub.AddUser(user)
  print response
  response = protobuf_to_dict(response)
  if response["Message"] == "failed!":
    abort(500)
  return jsonify(response), 200

@app.route("/users/<string:name>", methods=["PUT", "PATCH"])
def update_users(name):
  if not request.json:
    abort(400)
  if 'Name' in request.json and not request.json['Name'] == name:
    abort(400)
  user_name = user_pb2.User_Name(Name=name)
  val = stub.GetUser(user_name)
  user = protobuf_to_dict(val)
  if user:
    if request.method == "PUT":
      if "Occupation" in request.json and "Hobbies" in request.json:
        user["Occupation"] = request.json["Occupation"]
        user["Hobbies"] = request.json["Hobbies"]
      else:
        abort(400)
    elif request.method == "PATCH":
      if "Occupation" in request.json:
        user["Occupation"] = request.json["Occupation"]
      if "Hobbies" in request.json:
        user["Hobbies"] = request.json["Hobbies"]
    user = user_pb2.User(**user)
    response = stub.UpdateUser(user)
    response = protobuf_to_dict(response)
    if response["Message"] == "failed!":
      abort(500)
    return jsonify(response), 200
  else:
    abort(404)


if __name__ == "__main__":
  go_service_host = sys.argv[1]
  print go_service_host 
  channel = grpc.insecure_channel(str(go_service_host) + ':50051')
  stub = user_pb2_grpc.UserdbStub(channel)
  app.run(host='0.0.0.0', port=5000, debug=True, threaded=True,
          ssl_context=context)
