import json
import boto3
import random
import urllib3

client = boto3.client('apigatewaymanagementapi', endpoint_url="https://0tq3vpyco3.execute-api.us-east-1.amazonaws.com/production")

def lambda_handler(event, context):
    #get the connection ID from the event
    connectionId = event["requestContext"]["connectionId"]
    #Scan the Dynamodb table and get all the Word table items 
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('word')
    response = table.scan()
    data = response['Items']
    #get the random word from the item
    random_word = data[random.randint(0, len(response['Items'])-1)] 
    #Post the response to API GateWay
    response = client.post_to_connection(ConnectionId=connectionId, Data=json.dumps(random_word['word']).encode('utf-8'))
    return {
        'statusCode': 200,
        'body': json.dumps(random_word['word'])
       
    }
