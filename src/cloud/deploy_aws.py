import boto3
import os

def upload_model_to_s3(bucket_name: str, model_path: str):
    """
    Uploads the model file to an S3 bucket.

    Args:
        bucket_name (str): Your target S3 bucket.
        model_path (str): Local path to the model (e.g. models/diabetes_model.h5)
    """
    s3 = boto3.client("s3")

    try:
        model_filename = os.path.basename(model_path)
        s3.upload_file(model_path, bucket_name, model_filename)
        print(f"✅ Uploaded {model_filename} to s3://{bucket_name}/{model_filename}")
    except Exception as e:
        print(f"❌ Upload failed: {e}")
