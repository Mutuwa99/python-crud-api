import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Items')

def create(event, context):
    data = json.loads(event['body'])
    item_id = data['id']
    item_name = data['name']
    item_price = data['price']

    try:
        table.put_item(
            Item={
                'id': item_id,
                'name': item_name,
                'price': item_price
            }
        )
        response = {
            'statusCode': 200,
            'body': json.dumps({'message': 'Item created successfully'})
        }
    except ClientError as e:
        response = {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

    return response