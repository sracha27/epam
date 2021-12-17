import json
import boto3
import random
import urllib3

client = boto3.client('apigatewaymanagementapi', endpoint_url="https://0tq3vpyco3.execute-api.us-east-1.amazonaws.com/production")

def lambda_handler(event, context):
    print(event)
    return {
        'statusCode': 200,
        'body': json.dumps("Hello")
       
    }
