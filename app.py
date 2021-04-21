# Importing necessary libraries

from flask import Flask
import boto3
from boto3.session import Session
from flask import Flask, request, render_template 

# Constructor
app = Flask(__name__)

# Setting app route
@app.route("/", methods =["GET","POST"])

# Index Fuction
def index():
    files = []
    if request.method == "POST":
        dir = request.form.get("fname")
        files=list_files(dir)
    return render_template("index.html",files=files)  

# Function to get the filenames in the folders of AWS Bucket
def list_files(dir):
    # AWS Credentials
    AWS_ACCESS_KEY='AKIAYHIIKXEA666KEZGF'
    AWS_SECRET_ACCESS_KEY='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'
    AWS_STORAGE_BUCKET_NAME='1717-mybucket'
    AWS_S3_REGION_NAME='ap-south-1'
    bucket_name='1717-mybucket'

    file_list=[]
    session = Session(aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    s3 = session.resource('s3')
    for obj in s3.Bucket(bucket_name).objects.filter(Prefix=dir).all():
        file_name=obj.key.split(dir + "/")[1]
        print(file_name)
        if len(file_name)>0:
            file_list.append(file_name)
    return file_list

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8085)