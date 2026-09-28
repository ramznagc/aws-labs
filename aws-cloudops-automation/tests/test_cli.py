from unittest.mock import patch

from src.cli import main


@patch("src.cli.list_instances")
def test_cli(mock_list_instances, capsys):
    mock_list_instances.return_value = [
        {
            "id": "i-1234567890",
            "name": "web-server",
            "type": "t3.micro",
            "state": "running",
            "private_ip": "10.0.1.10",
            "public_ip": "54.10.20.30",
        }
    ]

    with patch("sys.argv", ["cli.py", "--region", "us-east-1"]):
        main()

    output = capsys.readouterr().out

    assert "Region: us-east-1" in output
    assert "Total instances: 1" in output
    assert "web-server" in output
    assert "t3.micro" in output
    assert "running" in output
