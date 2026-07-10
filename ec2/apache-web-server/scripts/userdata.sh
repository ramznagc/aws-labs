#!/bin/bash

# Update system
dnf update -y

# Install Apache
dnf install -y httpd

# Get current date and time
DATE_TIME=$(date)

# Create index page
cat <<EOF >/var/www/html/index.html
<html>
<head>
    <title>My First Web Server</title>
</head>
<body>
    <h1>Hello Everyone from My First Web Server</h1>
    <p>This server was created at: <b>$DATE_TIME</b></p>
</body>
</html>
EOF

# Start and enable Apache
systemctl enable httpd
systemctl start httpd