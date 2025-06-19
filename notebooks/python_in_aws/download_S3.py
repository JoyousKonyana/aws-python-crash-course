import boto3

s3 = boto3.client('s3')

def download_file(bucket, key, local_path):
    try:
        s3.download_file(bucket, key, local_path)
        print(f"✅ Downloaded to {local_path}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    download_file("your-bucket-name", "input/data.csv", "downloaded.csv")