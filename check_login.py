from flask import Flask, render_template, request, redirect,  url_for

app = Flask(__name__)

@app.route('/')
def home():
     #userid = request.args.get("#token_id")
     print(request.full_path)
     print(request.path)
     print(request.script_root)
     print(request.url)
     print(request.base_url)
     print(request.url_root)
     print(request.args.get("token_id"))
     return("hi")
    
    
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80, debug = True)