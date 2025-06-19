import boto3

# Replace with your bucket name
bucket_name = 'ryan-s3-test-bucket'  # <-- your actual bucket
file_name = 'test_upload.txt'
object_name = 'uploaded_test.txt'  # How it'll appear in S3

# Create S3 client
s3 = boto3.client('s3')

# Upload the file
try:
    s3.upload_file(file_name, bucket_name, object_name)
    print(f"✅ Uploaded {file_name} to {bucket_name}/{object_name}")
except Exception as e:
    print(f"❌ Upload failed: {e}")
