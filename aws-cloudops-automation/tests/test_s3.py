from datetime import datetime, timezone
from unittest.mock import patch

from src.inventory.s3 import list_buckets


@patch("src.inventory.s3.boto3.client")
def test_list_buckets(mock_client):
    mock_s3 = mock_client.return_value

    mock_s3.list_buckets.return_value = {
        "Buckets": [
            {
                "Name": "test-bucket",
                "CreationDate": datetime(
                    2026,
                    9,
                    29,
                    tzinfo=timezone.utc,
                ),
            }
        ]
    }

    result = list_buckets()

    assert len(result) == 1
    assert result[0]["name"] == "test-bucket"
    assert result[0]["creation_date"] == "2026-09-29T00:00:00+00:00"

    mock_client.assert_called_once_with("s3")
