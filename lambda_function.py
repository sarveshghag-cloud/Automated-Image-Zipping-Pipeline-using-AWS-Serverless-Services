
import boto3
import zipfile
import os

s3 = boto3.client('s3')

DEST_BUCKET = "compressed-images-zip-bucket"

def lambda_handler(event, context):

    source_bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    file_name = object_key.split('/')[-1]

    download_path = '/tmp/' + file_name
    zip_path = '/tmp/compressed-images.zip'

    # Download image from source bucket
    s3.download_file(source_bucket, object_key, download_path)

    # Create zip file
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        zipf.write(download_path, file_name)

    # Upload zip to destination bucket
    s3.upload_file(zip_path, DEST_BUCKET, 'compressed-images.zip')

    return {
        "statusCode": 200,
        "body": "Zip uploaded successfully"
    }