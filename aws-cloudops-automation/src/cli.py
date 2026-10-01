import argparse

from src.inventory.ec2 import list_instances
from src.inventory.s3 import list_buckets
from src.inventory.lambda_inventory import list_functions
from src.inventory.iam import list_users


def main():
    parser = argparse.ArgumentParser(description="AWS inventory")
    parser.add_argument(
        "--region",
        required=True,
        help="AWS region, for example us-east-1",
    )

    args = parser.parse_args()

    # EC2 Inventory
    instances = list_instances(args.region)

    print(f"Region: {args.region}")
    print(f"Total instances: {len(instances)}")
    print("-" * 40)

    for instance in instances:
        print(f"Instance ID: {instance['id']}")
        print(f"Name: {instance['name']}")
        print(f"Type: {instance['type']}")
        print(f"State: {instance['state']}")
        print(f"Private IP: {instance['private_ip'] or '-'}")
        print(f"Public IP: {instance['public_ip'] or '-'}")
        print("-" * 40)

    # S3 Inventory
    print()
    print("S3 Buckets:")
    print("-" * 40)

    buckets = list_buckets()

    for bucket in buckets:
        print(f"Bucket: {bucket['name']}")
        print(f"Created: {bucket['creation_date']}")
        print("-" * 40)

    # Lambda Inventory
    print()
    print("Lambda Functions:")
    print("-" * 40)

    functions = list_functions(args.region)

    for function in functions:
        print(f"Name: {function['name']}")
        print(f"Runtime: {function['runtime']}")
        print(f"Handler: {function['handler']}")
        print(f"State: {function['state']}")
        print("-" * 40)

    # IAM Inventory
    print()
    print("IAM Users:")
    print("-" * 40)

    users = list_users()

    for user in users:
        print(f"Name: {user['name']}")
        print(f"User ID: {user['id']}")
        print(f"ARN: {user['arn']}")
        print("-" * 40)


if __name__ == "__main__":
    main()
