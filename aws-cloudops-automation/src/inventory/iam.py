import boto3


def list_users():
    iam = boto3.client("iam")

    paginator = iam.get_paginator("list_users")

    users = []

    for page in paginator.paginate():
        for user in page["Users"]:
            users.append(
                {
                    "name": user["UserName"],
                    "id": user["UserId"],
                    "arn": user["Arn"],
                }
            )

    return users
