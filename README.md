##### siads_milestone_I - Owner: Yao Tong (tonyao@umich.edu) & Cydia Tsang (cydia@umich.edu)

##### ------------ To Get Data from DynamoDB ------------
###### 1. Go to src/data/dynamo_db_client.py to fill in the aws_secret_key. Could get the value of this aws_secret_key by contacting cydia135260@gmail.com
###### 2. Install boto3 if you do not have "pip install boto3"
###### 3. Run python command "python src/database/get_data.py" to get data from DynamoDB

###### ------------ To Upload Data to DynamoDB ------------
###### 1. Go to src/data/dynamo_db_client.py to fill in the aws_secret_key. Could get the value of this aws_secret_key by contacting cydia135260@gmail.com
###### 2. Install boto3 if you do not have "pip install boto3"
###### 3. Run python command "python src/database/upload_trending_data.py" to upload data to DynamoDB

###### ------------ To access our main project ------------
###### 1. pip install jupyter
###### 2. jupyter notebook
###### 3. Inside jupyter notebook, click project.ipynb 