import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Items')

def update(event, context):
    item_id = event['pathParameters']['id']
    data = json.loads(event['body'])
    item_name = data['name']
    item_price = data['price']

    try:
        response = table.update_item(
            Key={'id': item_id},
            UpdateExpression='set #name = :n, #price = :p',
            ExpressionAttributeNames={'#name': 'name', '#price': 'price'},
            ExpressionAttributeValues={':n': item_name, ':p': item_price},
            ReturnValues='UPDATED_NEW'
        )
        updated_item = response['Attributes']
        response = {
            'statusCode': 200,
            'body': json.dumps(updated_item)
        }
    except ClientError as e:
        response = {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

    return response