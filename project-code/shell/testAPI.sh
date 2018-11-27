##### create function ##########
#curl -X POST -d @/opt/cloudmesh/fa18-516-08/project-code//test/fun.json -H "Content-Type: application/json" http://0.0.0.0:8080/lambda/function/curltest
##### Test to invoke Lambda #########
##### list functions ############
#curl -X GET -H "Content-Type: application/json" http://0.0.0.0:8080/lambda/functions
##### list function by name #######
#curl -X GET -H "Content-Type: application/json" http://0.0.0.0:8080/lambda/function/curltest
##### delete function #############
#curl -X DELETE -H "Content-Type: application/json" http://0.0.0.0:8080/lambda/function/curltest