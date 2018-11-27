#####setup #######
mkdir -p /opt/cloudmesh


#### get all files from Github ########
cd /opt/cloudmesh
git clone https://github.com/cloudmesh-community/fa18-516-08

cd /opt/cloudmesh/fa18-516-08/project-code
##### install requirements.txt #####
sudo pip3 install -r requirements.txt



