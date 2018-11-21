import json
import boto3


def search_text(event, context):
    s3 = boto3.client('s3')
    bucket = 'XXXXX'
    key = event.get("filename")
    search_result = []
    search_result_dict = {}
    substr = event.get("search")
    l_substr = substr.lower()
    filepath = '/tmp/temp.txt'

    try:
        # data = s3.get_object(Bucket=bucket, Key=key)
        s3.download_file(bucket, key, filepath)
        # content = data['Body'].read().decode("utf-8")
        with open(filepath, 'rt') as read_file:
            for linenum, line in enumerate(read_file):
                if line.lower().find(l_substr) != -1:
                    search_result.append(("Line Number " + str(linenum), line.rstrip('\n')))
                    # print(store_search)

        search_result_dict.update(search_result)
        return (search_result_dict)
    except Exception as err:
        # print(err)
        raise err