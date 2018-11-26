import connexion
import six

from swagger_server.models.search import SEARCH  # noqa: E501
from swagger_server import util
from flask import jsonify
import boto3,json
import sys
import botocore.response as br
def invoke_lambda(text,filename):
    client = boto3.client('lambda',aws_access_key_id='XXXXXX',aws_secret_access_key='YYYYYY',region_name='us-east-2')
    payload = {"search" : text,"filename":filename}
    payload = json.dumps(payload)
    print(payload)
    response = client.invoke(FunctionName='xxxxx',InvocationType='RequestResponse',LogType='None',Payload=payload)
    #res = response.get("Payload")
    #print(res)
    res = (response['Payload'].read().decode("utf-8"))
    return res


def search_invoke_lambda(text, filename):  # noqa: E501
    """search_invoke_lambda

     # noqa: E501

    :param text:
    :type text: str
    :param filename:
    :type filename: str

    :rtype: SEARCH
    """
    return jsonify(SEARCH(invoke_lambda(text,filename)))