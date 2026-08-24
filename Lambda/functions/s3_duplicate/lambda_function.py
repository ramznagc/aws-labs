import json
import os

import boto3

s3_client = boto3.client("s3")

DESTINATION_BUCKET = os.environ.get(
    "DESTINATION_BUCKET",
    "ondia.destination.lambda",
)


def lambda_handler(event, context):
    """Copy the object that triggered the Lambda function to another bucket."""
    print("Event:", json.dumps(event))

    record = event["Records"][0]
    source_bucket = record["s3"]["bucket"]["name"]
    object_key = record["s3"]["object"]["key"]

    copy_source = {
        "Bucket": source_bucket,
        "Key": object_key,
    }

    s3_client.copy_object(
        CopySource=copy_source,
        Bucket=DESTINATION_BUCKET,
        Key=object_key,
    )

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "Object copied successfully",
                "source_bucket": source_bucket,
                "destination_bucket": DESTINATION_BUCKET,
                "key": object_key,
            }
        ),
    }
