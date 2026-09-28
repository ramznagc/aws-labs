import boto3


def list_instances(region):
    ec2 = boto3.client("ec2", region_name=region)

    response = ec2.describe_instances()

    instances = []

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            name = "-"

            for tag in instance.get("Tags", []):
                if tag["Key"] == "Name":
                    name = tag["Value"]

            instances.append(
                {
                    "id": instance["InstanceId"],
                    "name": name,
                    "type": instance["InstanceType"],
                    "state": instance["State"]["Name"],
                    "private_ip": instance.get("PrivateIpAddress"),
                    "public_ip": instance.get("PublicIpAddress"),
                }
            )

    return instances
