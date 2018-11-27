#####setup pyenv #######
mkdir /cloudmesh/fa18-516-08/project-code
mkdir /cloudmesh/fa18-516-08/project-code/LambdaDeployment /cloudmesh/fa18-516-08/project-code/templates


#### get all files from Github ########
cd /cloudmesh/fa18-516-08/project-code
wget https://github.com/cloudmesh-community/fa18-516-08/blob/master/project-code/lambda_app.py
wget https://github.com/cloudmesh-community/fa18-516-08/blob/master/project-code/lambda.py
wget https://github.com/cloudmesh-community/fa18-516-08/blob/master/project-code/lambda.yaml
wget https://github.com/cloudmesh-community/fa18-516-08/blob/master/project-code/requirements.txt
wget https://github.com/cloudmesh-community/fa18-516-08/blob/master/project-code/create_lambda_basic_exec_role.py
wget https://github.com/cloudmesh-community/fa18-516-08/blob/master/project-code/config.py
cd templates
wget https://github.com/cloudmesh-community/fa18-516-08/blob/master/project-code/templates/lambda.html
wget https://github.com/cloudmesh-community/fa18-516-08/blob/master/project-code/templates/upload.html
cd ../

##### install requirements.txt #####
pip3 install -r requirements.txt
##### deployment package upload #####
cd LambdaDeployment

##### run lambda_app.py ########
##### create function ##########
curl -X POST -d @fun.json -H "Content-Type: application/json" http://127.0.0.1:5555/lambda/function/curltest
##### Test to invoke Lambda #########
##### list functions ############
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:5555/lambda/functions
##### list function by name #######
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:5555/lambda/function/curltest
##### delete function #############
curl -X DELETE -H "Content-Type: application/json" http://127.0.0.1:5555/lambda/function/curltest
