import boto3
import zipfile
import os
import urllib.parse
from datetime import datetime

s3 = boto3.client('s3')

DEST_BUCKET = "compressed-images-zip-bucket"

def lambda_handler(event, context):
    try:
        for record in event['Records']:

            source_bucket = record['s3']['bucket']['name']
            object_key = urllib.parse.unquote_plus(record['s3']['object']['key'])

            file_name = os.path.basename(object_key)

            # Unique zip file name (timestamp)
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            zip_filename = f"{file_name}-{timestamp}.zip"

            download_path = f"/tmp/{file_name}"
            zip_path = f"/tmp/{zip_filename}"

            print(f"Processing file: {file_name}")

            # Download file
            s3.download_file(source_bucket, object_key, download_path)

            # Create zip
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(download_path, file_name)

            # Upload zip to destination bucket
            s3.upload_file(zip_path, DEST_BUCKET, zip_filename)

            print(f"Uploaded zip: {zip_filename}")

            # Clean up (important for Lambda space)
            os.remove(download_path)
            os.remove(zip_path)

        return {
            "statusCode": 200,
            "body": "Zip created and uploaded successfully"
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            "statusCode": 500,
            "body": "Error processing file"
        }