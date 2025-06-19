# AWS S3 Upload with Python

This is a simple project that uploads a file to an AWS S3 bucket using Python and `boto3`.

The project:
- Uses AWS IAM user credentials securely (via `aws configure`)
- Uploads a local file (`test_upload.txt`) to an S3 bucket
- Demonstrates working knowledge of AWS SDK, permissions, and scripting

Folder Contents
- `upload_to_s3.py`: Python script for uploading a file to S3
- `test_upload.txt`: Example file to upload

How to Run:
1. Make sure you have AWS credentials set up:
   aws configure
2. pip install boto3
3. python upload_to_s3.py


What I Learned
How to securely interact with AWS from Python

How to configure and use IAM programmatic access

How to upload and manage objects in S3

Basic use of Git and GitHub for project sharing
