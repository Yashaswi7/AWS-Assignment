# Create S3 bucket 1717-mybucket (Please ensure not to open the bucket to public)
![Screenshot (10)](https://user-images.githubusercontent.com/73656498/115603046-50be3380-a2fd-11eb-9bfa-f0f7317fdc18.png)


# Create files inside the buckets A,B,C.
Putting file1.py in A, file2.py in B, file3.py in C folders


![Screenshot (11)](https://user-images.githubusercontent.com/73656498/115603370-b3173400-a2fd-11eb-8b96-44ed521e3a20.png)
# Creating a flask app that gets the folder name and lists the filename present in the corresponding folder. (Use Boto3 for reading the contents of the folder) and test the code in local 

## Steps
a. Install awscli
b. Open the terminal and enter the following command
   aws --configure
c. Install flask   
d. Clone the repository and go to the directory
e. Run the app in local using command python3 app.py

![Screenshot (14)](https://user-images.githubusercontent.com/73656498/115605123-c2977c80-a2ff-11eb-81b7-9f9648b36e34.png)

# Open an ec2-instance and while creating the instance keep ssh port as it is and add new rule as custom TCP and port 8085 to allow traffic

![Screenshot (15)](https://user-images.githubusercontent.com/73656498/115605368-0ee2bc80-a300-11eb-8ac5-bf254ccd2b33.png)

# You can use this ssh command to login into ec2 instance using your local machine

![Screenshot (16)](https://user-images.githubusercontent.com/73656498/115605611-59643900-a300-11eb-8c77-534e88dd2642.png)

# After that install all the required packages python,flask,boto3,nginx,gunicorn and then copy the file content of your local app into ec2 instance

# Then run python3 app.py

@Your url will be public ip adress:8085. This url will show your flask application

## Billing information
![Screenshot (8)](https://user-images.githubusercontent.com/73656498/115606248-19ea1c80-a301-11eb-917c-bb85ac0bd986.png)
![Screenshot (9)](https://user-images.githubusercontent.com/73656498/115606295-266e7500-a301-11eb-80df-de9b77fee647.png)

# URL [http://13.233.18.194:8085/]{http://13.233.18.194:8085/}
