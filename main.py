
import json
import boto3

s3 = boto3.resource('s3')
def lambda_handler(event, context):
    print(event)
    dump = json.loads(json.dumps(event))
    fileName = dump['image']
    print(fileName)

    bucket='cloudcomputingdemo-2'

    client=boto3.client('rekognition')
    text=client.detect_text(Image={'S3Object': {'Bucket':bucket,'Name':str(fileName)}})
    res = {
        "textFound": text
    }
    return res