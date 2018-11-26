import os

class AWS:
    AWS_ACCESS_KEY_ID = 'XXXXXXXXX'
    AWS_SECRET_ACCESS_KEY = 'XXXXXXX'
    AWS_S3_BUCKET_NAME ='XXXXXXXX'
    AWS_DEFAULT_REGION='us-east-2'

class HOST:
    HOSTNAME = ''
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    TGT_DIR = os.path.join(ROOT_DIR,'LambdaDeployment/')
class Runenv:
    runenv = ['nodejs','nodejs4.3','nodejs6.10','nodejs8.10','java8','python2.7','python3.6','python3.7','dotnetcore1.0','dotnetcore2.0','dotnetcore2.1','nodejs4.3-edge','go1.x']

class AWS_POLICY:

    ############## LAMBDA BASIC EXECUTION POLICY #####################
    role = "Lambda_Basic_Exec5"
    policy = {"Version":"2012-10-17","Statement":[{"Sid": "","Effect":"Allow","Principal":{"Service":"lambda.amazonaws.com"},"Action":["sts:AssumeRole"]}]}


    ############## END OF BASIC POLICY #################################