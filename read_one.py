import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Items')

def read_one(event, context):
    item_id = event['pathParameters']['id']

    try:
        response = table.get_item(Key={'id': item_id})
        item = response.get('Item')
        if item:
            response = {
                'statusCode': 200,
                'body': json.dumps(item)
            }
        else:
            response = {
                'statusCode': 404,
                'body': json.dumps({'error': 'Item not found'})
            }
    except ClientError as e:
        response = {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

    return response