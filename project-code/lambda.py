#import all packages
import boto3
import config
import json
from botocore.exceptions import ClientError

client = boto3.client('lambda', aws_access_key_id= config.AWS.AWS_ACCESS_KEY_ID,
                              aws_secret_access_key=config.AWS.AWS_SECRET_ACCESS_KEY, region_name=config.AWS.AWS_DEFAULT_REGION)

#Function to list all available AWS Lambda functions for a user account in a region

def list_aws_lambda():
        lfunctions = []
        response = client.list_functions()
        fname = response['Functions']
        for name in fname:
            lfunctions.append('FunctionName: ' + name['FunctionName'])
        return json.dumps(lfunctions)

if __name__ == "__main__":
    print(list_aws_lambda())


#Function to list AWS Lambda function by name:

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

if __name__ == "__main__":
    print(get_aws_lambda_by_name('SearchText'))

#Function to create AWS Lambda Function:
def create_aws_lambda(fname,renv):
    if renv in config.Runenv.runenv:
        Runtime = renv
    else:
        return "{Error : Unsupported Runtime Env}"
    #response = client.create_function(Functionname=fname,Runtime=Runtime,)


#Function to delete AWS Lambda Function:
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
if __name__ == "__main__":
    print(del_aws_lambda('hello'))
