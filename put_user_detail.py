from __future__ import print_function # Python 2/3 compatibility
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1') #, endpoint_url="http://localhost:8000")

table = dynamodb.Table('WebAppUserData')

table.put_item(
   Item={
       'userid': 'E0419074',
       'project': ['projectfolder1','projectfolder2'],
       'bucket':'my-lambda-2',
       'path':'NA'
    }
)