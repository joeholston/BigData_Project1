import csv, json

csvFile = open('Traffic_Violations.csv', 'r')
jsonFile = open('Traffic_Violations.json', 'w')

fields = ("Date Of Stop","Time Of Stop","Agency","SubAgency","Description","Location","Latitude","Longitude","Accident","Belts","Personal Injury","Property Damage","Fatal","Commercial License","HAZMAT","Commercial Vehicle","Alcohol","Work Zone","State","VehicleType","Year","Make","Model","Color","Violation Type","Charge","Article","Contributed To Accident","Race","Gender","Driver City","Driver State","DL State","Arrest Type","Geolocation")

reader = csv.DictReader(csvFile, fields)
for row in reader:
    json.dump(row, jsonFile)
    jsonFile.write('\n')
