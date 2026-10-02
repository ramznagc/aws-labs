import boto3


def list_alarms(region):
    cloudwatch = boto3.client("cloudwatch", region_name=region)

    response = cloudwatch.describe_alarms()

    alarms = []

    for alarm in response["MetricAlarms"]:
        alarms.append(
            {
                "name": alarm["AlarmName"],
                "state": alarm["StateValue"],
                "metric": alarm["MetricName"],
                "namespace": alarm["Namespace"],
            }
        )

    return alarms