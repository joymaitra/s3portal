from __future__ import print_function # Python 2/3 compatibility
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1') #, endpoint_url="http://localhost:8000")

table = dynamodb.Table('WebAppUserData')

table.put_item(
   Item={
       'userid': 'E0419074',
       'projects': [{'name':'folder3','path':'folder3'},{'name':'folder4','path':'folder4'},{'name':'folder5','path':'folder5'}]
    }
)