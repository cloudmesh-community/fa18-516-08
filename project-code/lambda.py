#import all packages
import boto3
import yaml
import os
from flask import request
from botocore.exceptions import ClientError
from create_lambda_basic_exec_role import get_role

# Load YAML config file
with open("config.yaml", 'r') as f:
    cfg = yaml.load(f)
AWS_ACCESS_KEY_ID = cfg['AWS']['AWS_ACCESS_KEY_ID']
AWS_DEFAULT_REGION = cfg['AWS']['AWS_DEFAULT_REGION']
AWS_SECRET_ACCESS_KEY = cfg['AWS']['AWS_SECRET_ACCESS_KEY']
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
TGT_DIR = os.path.join(ROOT_DIR,'test/')

# Setup boto3 client (AWS SDK) for lambda
client = boto3.client('lambda', aws_access_key_id= AWS_ACCESS_KEY_ID,
                              aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=AWS_DEFAULT_REGION)



# Function to list all available AWS Lambda functions for a user account in a region

def list_aws_lambda():
    response = client.list_functions()
    fname = response['Functions']
    return fname




# Function to list AWS Lambda function by name:

def get_aws_lambda_by_name(fname):
    try:
        response = client.get_function_configuration(FunctionName=fname)
        del response['ResponseMetadata']
        return response
    except ClientError as err:
        if err.response['Error']['Code'] == 'ResourceNotFoundException':
            e = "{Error : Function " + fname + " does not exist}"
            return e
        else:
            return "{Error: Unexpected Error}"



# Function to create AWS Lambda Function:

def create_aws_lambda(fname):
    ret = request.get_json()
    renv = ret['renv']
    pkg = ret['pkg']
    handler = ret['handler']
    cfile = ret['cfile']
    pkg = os.path.join(TGT_DIR, pkg)
    py_file = os.path.splitext(cfile)[0]

    Handler = py_file + "." + handler
    print(Handler)

    with open(pkg, 'rb') as f:
        zipped_code = f.read()
    try:
        response = client.create_function(FunctionName=fname, Runtime=renv,
                                          Role=get_role(),
                                          Handler=Handler, Code=dict(ZipFile=zipped_code))
        del response['ResponseMetadata']
        return response
    except ClientError as err:
        if err.response['Error']['Code'] == 'ResourceConflictException':
            e = "{Error : Function " + fname + " already exists}"
            return e
        else:
            # return "{Error: Unexpected Error}"
            return err




# Function to delete AWS Lambda Function:

def del_aws_lambda(fname):
    try:
        response = client.delete_function(FunctionName=fname)
        del response['ResponseMetadata']
        #return response
        return "{Message : Requested Function Deleted}"
    except ClientError as err:
        if err.response['Error']['Code'] == 'ResourceNotFoundException':
            e = "{Error : Function " + fname + " does not exist}"
            return e
        else:
            return "{Error: Unexpected Error}"


# Function to update  AWS Lambda Function:

def upd_aws_lambda(fname):

    ret = request.get_json()
    proplist = ['Description','Handler','MemorySize','Runtime','Role','Timeout']
    propdict= {k: ret[k] for k in proplist if k in ret}
    return propdict



# Function to Upload deployment package for creating Lambda Function

def upload():
    target_path = TGT_DIR
    print(target_path)
    if not os.path.isdir(target_path):
        os.mkdir(target_path)

    for f in request.files.getlist("pkg"):
        #f = request.files("file")
        print(f)
        filename = f.filename
        print(filename)
        dest = "/".join([target_path,filename])
        f.save(dest)
    return "Zip File Deployment Package Uploaded Successfully"
