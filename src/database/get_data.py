import sys, os
sys.path.append(os.getcwd() + "/src")
from pj_config.dynamo_db_client import get_dynamo_db_client

dynamodb = get_dynamo_db_client()

# Retrieve the item
response = dynamodb.scan(
    TableName='tiktok_trending',
    Limit=10  # Limit the result to 10 items
)

if response:
    print(response)
else:
    print("Item not found.")