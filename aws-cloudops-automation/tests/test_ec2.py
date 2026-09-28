from unittest.mock import patch

from src.inventory.ec2 import list_instances


@patch("src.inventory.ec2.boto3.client")
def test_list_instances(mock_client):
    mock_ec2 = mock_client.return_value

    mock_ec2.describe_instances.return_value = {
        "Reservations": [
            {
                "Instances": [
                    {
                        "InstanceId": "i-1234567890",
                        "InstanceType": "t3.micro",
                        "State": {"Name": "running"},
                        "PrivateIpAddress": "10.0.1.10",
                        "PublicIpAddress": "54.10.20.30",
                        "Tags": [
                            {"Key": "Name", "Value": "web-server"}
                        ],
                    }
                ]
            }
        ]
    }

    result = list_instances("us-east-1")

    assert len(result) == 1
    assert result[0]["id"] == "i-1234567890"
    assert result[0]["name"] == "web-server"
    assert result[0]["type"] == "t3.micro"
    assert result[0]["state"] == "running"
    assert result[0]["private_ip"] == "10.0.1.10"
    assert result[0]["public_ip"] == "54.10.20.30"

    mock_client.assert_called_once_with(
        "ec2",
        region_name="us-east-1",
    )
