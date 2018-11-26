import json
import boto3
import config
from botocore.exceptions import ClientError

iam_client = boto3.client('iam',aws_access_key_id= config.AWS.AWS_ACCESS_KEY_ID,
                              aws_secret_access_key=config.AWS.AWS_SECRET_ACCESS_KEY, region_name=config.AWS.AWS_DEFAULT_REGION)


def get_role():
    try:
        iam_role = iam_client.get_role(RoleName=config.AWS_POLICY.role)

        return (iam_role['Role']['Arn'])

    except ClientError as err:
        # print(err.response)
        if err.response['Error']['Code'] == 'NoSuchEntity':
            iam_client.create_role(RoleName=config.AWS_POLICY.role,AssumeRolePolicyDocument=json.dumps(config.AWS_POLICY.policy))
            iam_role = iam_client.get_role(RoleName=config.AWS_POLICY.role)
            return (iam_role['Role']['Arn'])
if __name__ =="__main__":
    get_role()


