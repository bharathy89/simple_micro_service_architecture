# simple_micro_service
mongo_db->go_server(grpc)->python_app(flask)

How to run:

chmod +x ./deploy_micro

./deploy_micro

What does this do:

1. This is a simple micro service application. python_app contains a flask server
hosting /users route.

2. python_app interfaces with go_server via grpc.

3. go_server is a middle layer between db and python_app. It makes the necessary
db calls.

4. All the services are running on different containers. ( duh!)

5. you can run ./deploy_micro script to deploy.

6. you access the python_app by making rest api calls [GET, POST, PUT, PATCH, DELETE] to https://127.0.0.1:5000/users

sample calls you can make 

curl -X POST -H "Content-Type: application/json" -d '{
  "Hobbies": [
    "football",
    "painting"
  ],
  "Name": "John Doe",
  "Occupation": "Software Engineer"
}' "https://127.0.0.1:5000/users"
