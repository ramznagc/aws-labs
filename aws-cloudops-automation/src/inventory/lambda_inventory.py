import boto3


def list_functions(region):
    lambda_client = boto3.client("lambda", region_name=region)

    response = lambda_client.list_functions()

    functions = []

    for function in response["Functions"]:
        functions.append(
            {
                "name": function["FunctionName"],
                "runtime": function["Runtime"],
                "handler": function["Handler"],
                "state": function.get("State"),
            }
        )

    return functions