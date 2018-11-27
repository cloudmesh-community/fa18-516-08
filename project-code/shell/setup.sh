#####setup #######
mkdir -p /opt/cloudmesh/fa18-516-08/project-code
mkdir -p /opt/cloudmesh/fa18-516-08/project-code/test
mkdir -p /opt/cloudmesh/fa18-516-08/project-code/templates


#### get all files from Github ########
cd
cd /opt/cloudmesh/fa18-516-08/project-code
wget -N https://raw.githubusercontent.com/cloudmesh-community/fa18-516-08/master/project-code/lambda_app.py
wget -N https://raw.githubusercontent.com/cloudmesh-community/fa18-516-08/master/project-code/lambda.py
wget -N https://raw.githubusercontent.com/cloudmesh-community/fa18-516-08/master/project-code/lambda.yaml
wget -N https://raw.githubusercontent.com/cloudmesh-community/fa18-516-08/master/project-code/requirements.txt
wget -N https://raw.githubusercontent.com/cloudmesh-community/fa18-516-08/master/project-code/create_lambda_basic_exec_role.py
wget -N https://raw.githubusercontent.com/cloudmesh-community/fa18-516-08/master/project-code/config.py
cd templates
wget -N https://raw.githubusercontent.com/cloudmesh-community/fa18-516-08/master/project-code/templates/lambda.html
wget -N https://raw.githubusercontent.com/cloudmesh-community/fa18-516-08/master/project-code/templates/upload.html
cd ../test
wget -N https://raw.githubusercontent.com/cloudmesh-community/fa18-516-08/master/project-code/test/fun.json
cd ../

##### install requirements.txt #####
sudo pip3 install -r requirements.txt
##### deployment package upload #####
cd test
wget -N https://github.com/cloudmesh-community/fa18-516-08/raw/master/project-code/test/hello.zip
cd ../


