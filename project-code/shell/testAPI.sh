##### create function ##########
#curl -X POST -d @fun.json -H "Content-Type: application/json" http://127.0.0.1:5555/lambda/function/curltest
##### Test to invoke Lambda #########
##### list functions ############
#curl -X GET -H "Content-Type: application/json" http://127.0.0.1:5555/lambda/functions
##### list function by name #######
#curl -X GET -H "Content-Type: application/json" http://127.0.0.1:5555/lambda/function/curltest
##### delete function #############
#curl -X DELETE -H "Content-Type: application/json" http://127.0.0.1:5555/lambda/function/curltest