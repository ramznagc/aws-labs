from unittest.mock import patch

from src.inventory.cloudwatch import list_alarms


@patch("src.inventory.cloudwatch.boto3.client")
def test_list_alarms(mock_client):
    mock_cloudwatch = mock_client.return_value

    mock_cloudwatch.describe_alarms.return_value = {
        "MetricAlarms": [
            {
                "AlarmName": "HighCPU",
                "StateValue": "OK",
                "MetricName": "CPUUtilization",
                "Namespace": "AWS/EC2",
            }
        ]
    }

    result = list_alarms("us-east-1")

    assert len(result) == 1
    assert result[0]["name"] == "HighCPU"
    assert result[0]["state"] == "OK"
    assert result[0]["metric"] == "CPUUtilization"
    assert result[0]["namespace"] == "AWS/EC2"

    mock_client.assert_called_once_with(
        "cloudwatch",
        region_name="us-east-1",
    )
