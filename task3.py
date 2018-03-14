# The fix you gave us didn't work, this seemed to fix the timezone issue
import os
os.environ["TZ"] = "UTC"

import boto3

# Connect to local DynamoDB instance
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8080')

table = dynamodb.Table('violations')

def findByDate(searchDate):

def countOutOfStateCars():
    response = table.query(
        KeyConditionExpression=Key('Driver State').ne('MD')
    )

def findWorstOwners():
