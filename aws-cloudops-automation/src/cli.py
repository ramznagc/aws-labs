import argparse

from src.inventory.ec2 import list_instances


def main():
    parser = argparse.ArgumentParser(description="AWS EC2 inventory")
    parser.add_argument(
        "--region",
        required=True,
        help="AWS region, for example us-east-1",
    )

    args = parser.parse_args()

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


if __name__ == "__main__":
    main()
