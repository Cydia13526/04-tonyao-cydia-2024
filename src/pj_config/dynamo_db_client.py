import boto3
from cryptography.fernet import Fernet

def encrypt_access_key():
    key = Fernet.generate_key()
    with open("key.txt", "wb") as file:
        file.write(key)
    cipher_suite = Fernet(key)

    aws_access_key = cipher_suite.encrypt('AKIA45YHIOUEL552LTSU'.encode())
    with open("aws_access_key.txt", "wb") as file:
        file.write(aws_access_key)

    aws_secret_key = cipher_suite.encrypt('7TvJooiPPitNepeSMiNofOaASyx/NU2h+/8a1kgA'.encode())
    with open("aws_secret_key.txt", "wb") as file:
        file.write(aws_secret_key)


def get_dynamo_db_client():
    with open("key.txt", "rb") as file:
        key = file.read()
    cipher_suite = Fernet(key)
    with open("aws_access_key.txt", "rb") as file:
        aws_access_key_encrypted_string = file.read()

    aws_access_key = cipher_suite.decrypt(aws_access_key_encrypted_string).decode()
    with open("aws_secret_key.txt", "rb") as file:
        aws_secret_key_encrypted_string = file.read()
    aws_secret_key = cipher_suite.decrypt(aws_secret_key_encrypted_string).decode()
    aws_region = 'us-east-1'

    # Create a DynamoDB client
    return boto3.client('dynamodb', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=aws_region)
