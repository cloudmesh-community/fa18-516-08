import json
import boto3
import yaml
from botocore.exceptions import ClientError

# Load YAML config file
with open("config.yaml", 'r') as f:
    cfg = yaml.load(f)
AWS_ACCESS_KEY_ID = cfg['AWS']['AWS_ACCESS_KEY_ID']
AWS_DEFAULT_REGION = cfg['AWS']['AWS_DEFAULT_REGION']
AWS_SECRET_ACCESS_KEY = cfg['AWS']['AWS_SECRET_ACCESS_KEY']
role = cfg['AWS_POLICY']['role']
policy = cfg['AWS_POLICY']['policy']

# Create IAM Client
iam_client = boto3.client('iam',aws_access_key_id=AWS_ACCESS_KEY_ID,
                              aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=AWS_DEFAULT_REGION)


def get_role():
    try:
        iam_role = iam_client.get_role(RoleName=role)

        return (iam_role['Role']['Arn'])

    except ClientError as err:
        # print(err.response)
        if err.response['Error']['Code'] == 'NoSuchEntity':
            iam_client.create_role(RoleName=role,AssumeRolePolicyDocument=json.dumps(policy))
            iam_role = iam_client.get_role(RoleName=role)
            return (iam_role['Role']['Arn'])
if __name__ =="__main__":
    get_role()


