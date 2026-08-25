import boto3

ec2 = boto3.client("ec2")

response = ec2.describe_instances()

instance_count = 0

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        instance_count += 1

        name = "-"

        for tag in instance.get("Tags", []):
            if tag["Key"] == "Name":
                name = tag["Value"]

        print(
            f"Instance ID: {instance['InstanceId']}"
        )
        print(
            f"Name: {name}"
        )
        print(
            f"Type: {instance['InstanceType']}"
        )
        print(
            f"State: {instance['State']['Name']}"
        )
        print(
            f"Private IP: {instance.get('PrivateIpAddress', '-')}"
        )
        print(
            f"Public IP: {instance.get('PublicIpAddress', '-')}"
        )
        print("-" * 40)

if instance_count == 0:
    print("No EC2 instances found in us-east-1.")

print(f"Total instances: {instance_count}")
