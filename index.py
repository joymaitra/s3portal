from flask import Flask, render_template, request, redirect,  url_for
import time
import boto3
from boto3.dynamodb.conditions import Key, Attr


'''
Variable list

'''
db_resource_nm='dynamodb'
region_nm = 'us-east-1'
user_tbl_nm = 'WebAppUserData'
user_tbl_key = 'userid'
user_tbl_project = "projects"
user_tbl_dspl_nm = "name"
param_url_token = 'userid'
return_err_msg = "not authorized user"
main_web_page = "index.html"


'''
Code begins
'''
app = Flask(__name__)
dynamodb = boto3.resource(db_resource_nm, region_name=region_nm)
table = dynamodb.Table(user_tbl_nm)


@app.route('/')
def home():
    folder_names =[]
    userid = request.args.get(param_url_token)
    if (userid == None):
        return return_err_msg
    response = table.query(
        KeyConditionExpression=Key(user_tbl_key).eq(userid)
    )
    for i in response["Items"]:
        for j in i[user_tbl_project]:
            folder_names.append(j[user_tbl_dspl_nm])
    print(folder_names)
    #folder_names = ["a","b","c","d"]
    if (len(folder_names)>0):
        return render_template(main_web_page, len = len(folder_names), folders = folder_names, user=userid)
    else:
        return return_err_msg


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
