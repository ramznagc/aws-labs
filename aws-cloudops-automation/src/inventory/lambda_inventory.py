import boto3


def list_functions(region):
    lambda_client = boto3.client("lambda", region_name=region)

    paginator = lambda_client.get_paginator("list_functions")

    functions = []

    for page in paginator.paginate():
        for function in page["Functions"]:
            functions.append(
                {
                    "name": function["FunctionName"],
                    "runtime": function["Runtime"],
                    "handler": function["Handler"],
                    "state": function.get("State"),
                }
            )

    return functions
