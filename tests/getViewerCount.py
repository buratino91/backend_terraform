import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ViewerCounter')


def lambda_handler(event, context):
    try:
        response = table.get_item(
            TableName='ViewerCounter',
            Key={
                'id': 'page_views'
            },
            ProjectionExpression='#c',
            ExpressionAttributeNames={
                '#c': 'Count'
            }
        )
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'message': 'Count value retrieved successfully',
                 'Count': response['Item']['Count']
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'message': 'Error retrieving count value',
                'error': str(e)
            })
        }