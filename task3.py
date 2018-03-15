# The fix you gave us didn't work, this seemed to fix the timezone issue
import os
os.environ["TZ"] = "UTC"

import boto3
from boto3.dynamodb.conditions import Key, Attr

# Connect to local DynamoDB instance
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8080')

table = dynamodb.Table('violations')


def findByDate(searchDate):
    response = table.scan(
        FilterExpression=Key('date_of_stop').eq(searchDate)
    )
    count = 0
    for i in response['Items']:
        count += 1
    return count


def countOutOfStateCars():
    response = table.scan(
        FilterExpression=Attr('driver_state').ne('MD')
    )
    count = 0
    for i in response['Items']:
        count += 1
    return count

#def findWorstOwners():

print("Date Search:", findByDate('08/29/2017'))
print("Out of state cars:", countOutOfStateCars())
