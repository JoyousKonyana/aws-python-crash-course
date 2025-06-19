import boto3

s3 = boto3.client('s3')

def upload_data_to_s3(bucket, file_key, local_file):
    try:
        s3.upload_file(local_file, bucket, file_key)
        print(f"✅ Uploaded to s3://{bucket}/{file_key}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    upload_data_to_s3("your-bucket-name", "input/data.csv", "data/load_shedding.csv")
