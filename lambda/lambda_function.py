import boto3
import json
import os
from urllib import request
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime

s3 = boto3.client('s3')
S3_BUCKET = 'jenkins-artifact-archive-safe'

def lambda_handler(event, context):
    print("✅ Lambda triggered.")
    print("📦 Raw Event:")
    print(json.dumps(event))

    for record in event.get('Records', []):
        print("➡️ Record received:", record)

        try:
            body = json.loads(record['body'])
            print("🧾 Parsed body:", body)

            file_url = body.get('file_url')
            if not file_url:
                print("❌ 'file_url' not found. Skipping.")
                continue

            # Fetch the file header first to get 'Last-Modified'
            req = request.Request(file_url, method='HEAD')
            with request.urlopen(req) as res:
                last_modified = res.headers.get('Last-Modified')

            if not last_modified:
                print("❌ No Last-Modified header found. Skipping.")
                continue

            file_time = parsedate_to_datetime(last_modified).replace(tzinfo=timezone.utc)
            now = datetime.now(timezone.utc)

            if now - file_time < timedelta(minutes=5):
                print(f"🕒 Skipping {file_url} (only {(now - file_time).seconds} seconds old)")
                continue

            # Proceed to download and upload
            file_name = os.path.basename(file_url)
            tmp_file = f'/tmp/{file_name}'

            print(f"⬇️ Downloading from: {file_url}")
            request.urlretrieve(file_url, tmp_file)

            print(f"⬆️ Uploading to: s3://{S3_BUCKET}/archived-artifacts/{file_name}")
            s3.upload_file(tmp_file, S3_BUCKET, f'archived-artifacts/{file_name}')
            print(f"✅ Upload successful: {file_name}")

        except Exception as e:
            print(f"🔥 Error while processing: {str(e)}")

    return {'statusCode': 200, 'body': 'Done'}
