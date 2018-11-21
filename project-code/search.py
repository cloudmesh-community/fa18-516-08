import boto3,json
import sys
import botocore.response as br
def invoke_lambda(text,filename):
    client = boto3.client('lambda',aws_access_key_id='XXXXX',aws_secret_access_key='YYYY',region_name='us-east-2')
    payload = {"search" : text,"filename":filename}
    payload = json.dumps(payload)
    print(payload)
    response = client.invoke(FunctionName='xxxxx',InvocationType='RequestResponse',LogType='None',Payload=payload)
    #res = response.get("Payload")
    #print(res)
    print(response['Payload'].read().decode("utf-8"))
    #t_text = br.StreamingBody(raw_stream=res,content_length=23).read(amt=None).decode("utf-8")
    #print (t_text)
if __name__ == "__main__":
    invoke_lambda(sys.argv[1])