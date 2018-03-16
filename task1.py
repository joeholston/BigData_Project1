# The fix you gave us didn't work, this seemed to fix the timezone issue
import os
os.environ["TZ"] = "UTC"

import boto3


# Connect to local DynamoDB instance
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

# Delete table if it is defined
try:
    table = dynamodb.Table('violations')
    table.delete()
    print("Table deleted")
except:
    print("Table not defined")

# Define table
table = dynamodb.create_table(
    TableName='violations',
    KeySchema=[
        {
            'AttributeName': 'date_of_stop',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'time_of_stop',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'date_of_stop',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'time_of_stop',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

makeIndex =[
    {"Create": {
            "IndexName": "make-index",
            "KeySchema": [{
                "AttributeName": "make",
                "KeyType": "HASH"
                }],
            'Projection': {
                'ProjectionType': "ALL",

                },
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
            }},
    ]
table.update(AttributeDefinitions=[
    {
        'AttributeName': 'date_of_stop',
        'AttributeType': 'S'
    },
    {
        'AttributeName': 'time_of_stop',
        'AttributeType': 'S'
    },
    {
        'AttributeName': 'make',
        'AttributeType': 'S'
    }
    ], GlobalSecondaryIndexUpdates=makeIndex)

print("Table created")
