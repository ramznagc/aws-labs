from unittest.mock import patch

from src.inventory.lambda_inventory import list_functions


@patch("src.inventory.lambda_inventory.boto3.client")
def test_list_functions(mock_client):
    mock_lambda = mock_client.return_value
    mock_paginator = mock_lambda.get_paginator.return_value

    mock_paginator.paginate.return_value = [
        {
            "Functions": [
                {
                    "FunctionName": "test-function",
                    "Runtime": "python3.12",
                    "Handler": "app.lambda_handler",
                    "State": "Active",
                }
            ]
        }
    ]

    result = list_functions("us-east-1")

    assert len(result) == 1
    assert result[0]["name"] == "test-function"
    assert result[0]["runtime"] == "python3.12"
    assert result[0]["handler"] == "app.lambda_handler"
    assert result[0]["state"] == "Active"

    mock_client.assert_called_once_with(
        "lambda",
        region_name="us-east-1",
    )

    mock_lambda.get_paginator.assert_called_once_with("list_functions")
