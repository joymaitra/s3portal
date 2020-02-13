from flask import Flask, render_template, request, redirect,  url_for
import time
import boto3
from boto3.dynamodb.conditions import Key, Attr

app = Flask(__name__)
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('WebAppUserData')


@app.route('/')
def home():
    folder_names =[]
    userid = request.args.get('userid')
    if (userid == None):
        return "not authorised user"
    response = table.query(
        KeyConditionExpression=Key('userid').eq(userid)
    )
    for i in response["Items"]:
        for j in i["project"]:
            folder_names.append(j)
    print(folder_names)
    #folder_names = ["a","b","c","d"]
    if (len(folder_names)>0):
        return render_template("index.html", len = len(folder_names), folders = folder_names, user=userid)
    else:
        return "not authorised user"


@app.route('/upload', methods=['POST'])
def upload():
    print("hi")
    time.sleep(5)
    print("bye")
    s3 = boto3.resource('s3')
    s3.Bucket('projectfolder1').put_object(Key = request.files['myfile'].filename, Body=request.files['myfile'])
    
    return("stop")



if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80, debug = True)
