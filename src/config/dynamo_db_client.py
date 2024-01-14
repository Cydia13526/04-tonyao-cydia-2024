import boto3


def get_dynamo_db_client():
    # Replace 'your_access_key', 'your_secret_key', and 'your_region' with your actual AWS credentials and region
    aws_access_key = 'AKIA45YHIOUEL552LTSU'
    aws_secret_key = ''
    aws_region = 'us-east-1'

    # Create a DynamoDB client
    return boto3.client('dynamodb', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=aws_region)
