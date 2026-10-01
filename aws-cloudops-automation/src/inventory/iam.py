import boto3


def list_users():
    iam = boto3.client("iam")

    response = iam.list_users()

    users = []

    for user in response["Users"]:
        users.append(
            {
                "name": user["UserName"],
                "id": user["UserId"],
                "arn": user["Arn"],
            }
        )

    return users