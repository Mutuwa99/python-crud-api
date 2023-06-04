import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Items')

def read_all(event, context):
    try:
        response = table.scan()
        items = response['Items']
        response = {
            'statusCode': 200,
            'body': json.dumps(items)
        }
    except ClientError as e:
        response = {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

    return response