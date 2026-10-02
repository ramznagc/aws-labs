import boto3


def list_alarms(region):
    cloudwatch = boto3.client("cloudwatch", region_name=region)

    paginator = cloudwatch.get_paginator("describe_alarms")

    alarms = []

    for page in paginator.paginate():
        for alarm in page["MetricAlarms"]:
            alarms.append(
                {
                    "name": alarm["AlarmName"],
                    "state": alarm["StateValue"],
                    "metric": alarm["MetricName"],
                    "namespace": alarm["Namespace"],
                }
            )

    return alarms
