import csv, json
import boto3
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

# Connect to local DynamoDB instance
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')



csvFile = open('Traffic_Violations.csv', 'r')
jsonFile = open('Traffic_Violations.json', 'w')

fields = ("Date Of Stop","Time Of Stop","Agency","SubAgency","Description",
    "Location","Latitude","Longitude","Accident","Belts","Personal Injury",
    "Property Damage","Fatal","Commercial License","HAZMAT","Commercial Vehicle",
    "Alcohol","Work Zone","State","VehicleType","Year","Make","Model","Color",
    "Violation Type","Charge","Article","Contributed To Accident","Race","Gender",
    "Driver City","Driver State","DL State","Arrest Type","Geolocation")



# Open the csv and skip the headers
reader = csv.DictReader(csvFile, fields)
next(reader, None)

dictList = []

for i, row in enumerate(reader):
    dictList.append(row)

#if i >= 5:
#
#json.dump(dictList, jsonFile, separators=(',', ':'), indent=4)
