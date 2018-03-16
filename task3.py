# The fix you gave us didn't work, this seemed to fix the timezone issue
import os
os.environ["TZ"] = "UTC"

import boto3, json, operator
from boto3.dynamodb.conditions import Key, Attr
from operator import itemgetter

# Connect to local DynamoDB instance
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

table = dynamodb.Table('violations')

def findByDate(searchDate):
    response = table.query(
        KeyConditionExpression=Key('date_of_stop').eq(searchDate)
    )
    results = []

    print('Time of Stop\tSubagency\tDescription')

    for i in response['Items']:
        print("%10s %30s %8s" % (i["time_of_stop"], i["subagency"], i["description"]))
        results.append({"time_of_stop" : i['time_of_stop'],
            "subagency" : i['subagency'],
            "description" : i['description']})

def countOutOfStateCars():
    response = table.scan(
        FilterExpression=Attr('driver_state').ne('MD')
    )
    count = 0
    for i in response['Items']:
        count += 1
    print("Out of state cars:", count)
    return count

def findWorstOwners():
    response = table.scan(
        FilterExpression=Attr('make').ne(' ')
    )
    makeCount = {}
    for i in response['Items']:
        if i['make'] in makeCount:
            makeCount[i['make']] += 1
        else:
            makeCount[i['make']] = 1
    sortedMakeCount = sorted(makeCount.items(), key=operator.itemgetter(1))
    print("The make with the most violations is- ", sortedMakeCount[len(sortedMakeCount) - 1])
    return sortedMakeCount[len(sortedMakeCount) - 1]

findByDate('08/29/2017')
countOutOfStateCars()
findWorstOwners()
