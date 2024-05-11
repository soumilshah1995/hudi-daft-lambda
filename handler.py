try:
    import unzip_requirements
except ImportError:
    pass

import os
import json
import sys
import daft
import boto3

print("all modules ok")


def lambda_handler(event={}, context=None):
    print("event")
    print(event)

    region = os.getenv("DEV_AWS_REGION")
    s3_path = os.getenv("DEV_S3_HUDI_PATH")

    session = boto3.session.Session(
        aws_access_key_id=os.getenv("DEV_AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("DEV_AWS_SECRET_ACCESS_KEY"),
        region_name=region
    )
    creds = session.get_credentials()

    io_config = daft.io.IOConfig(
        s3=daft.io.S3Config(
            access_key=creds.secret_key,
            key_id=creds.access_key,
            session_token=creds.token,
            region_name=region,
        )
    )

    df = daft.read_hudi(s3_path, io_config=io_config)
    df = df.where(df["_hoodie_partition_path"] == "CA").limit(2)
    data_dict = df.to_pydict()
    json_data = json.dumps(data_dict, default=str)  # Convert datetimes to strings
    return json_data
