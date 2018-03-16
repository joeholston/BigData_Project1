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

table = dynamodb.Table('violations')

csvFile = open('Traffic_Violations.csv', 'r')

fields = ("date_of_stop","time_of_stop","agency","subagency","description",
    "location","latitude","longitude","accident","belts","personal_injury",
    "property_damage","fatal","commercial_license","hazmat","commercial_vehicle",
    "alcohol","work_zone","state","vehicletype","year","make","model","color",
    "violation_type","charge","article","contributed_to_accident","race","gender",
    "driver_city","driver_state","dl_state","arrest_type","geolocation")



# Open the csv and skip the headers
reader = csv.DictReader(csvFile, fields)
next(reader, None)

items = []

for i, v in enumerate(reader):
    row = dict(v)
    print("Row:", i, "Partition: ", v['date_of_stop'], " Sort: ", v['location'])
    for key in list(row.keys()):
        if row[key] == "":
            print("Deleted:", key)
            del row[key]

    #try:
    table.put_item(Item=row)
    #except ClientError:

    if i >= 1000:
        break

csvFile.close()
