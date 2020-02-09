from flask import Flask, render_template, request, redirect,  url_for
import time
#import boto3

app = Flask(__name__)

@app.route('/')
def home():
    folder_names = ["a","b","c","d"]
    return render_template("index.html", len = len(folder_names), folders = folder_names)


@app.route('/upload', methods=['POST'])
def upload():
    print("hi")
    time.sleep(5)
    print("bye")
    
    return("stop")



if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
