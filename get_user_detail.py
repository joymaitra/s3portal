#from __future__ import print_function # Python 2/3 compatibility
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', region_name='us-east-1') #, endpoint_url="http://localhost:8000")

table = dynamodb.Table('WebAppUserData')

uin = input("enter user : ")
print("hi")
response = table.query(
    KeyConditionExpression=Key('userid').eq(uin)
    )

#print (response["Items"])
for i in response["Items"]:
    for j in i["project"]:
        print(j)