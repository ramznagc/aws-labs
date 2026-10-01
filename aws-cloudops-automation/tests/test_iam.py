from unittest.mock import patch

from src.inventory.iam import list_users


@patch("src.inventory.iam.boto3.client")
def test_list_users(mock_client):
    mock_iam = mock_client.return_value

    mock_iam.list_users.return_value = {
        "Users": [
            {
                "UserName": "test-user",
                "UserId": "AIDA123456789",
                "Arn": "arn:aws:iam::123456789012:user/test-user",
            }
        ]
    }

    result = list_users()

    assert len(result) == 1
    assert result[0]["name"] == "test-user"
    assert result[0]["id"] == "AIDA123456789"
    assert result[0]["arn"] == (
        "arn:aws:iam::123456789012:user/test-user"
    )

    mock_client.assert_called_once_with("iam")
