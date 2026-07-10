
# 🚀 Hands-on EC2-01: Install Apache Web Server on Amazon EC2 (Amazon Linux 2023)

A beginner-friendly hands-on lab that demonstrates how to deploy, configure, and automate an Apache HTTP Server on an Amazon EC2 instance.

---

## 📚 Table of Contents

- Overview
- Prerequisites
- Launch an EC2 Instance
- Connect via SSH
- Install Apache
- Customize the Default Web Page
- Create a Custom HTML Page
- Automate Installation with User Data
- Test the Server

---

## 📖 Overview

In this lab you will learn how to:

- Launch an Amazon EC2 instance
- Connect securely using SSH
- Install Apache HTTP Server
- Configure and manage the Apache service
- Deploy a custom HTML page
- Automate the installation using EC2 User Data

---

## ⚙️ Prerequisites

- AWS Account
- EC2 Key Pair (.pem)
- Security Group allowing:
  - SSH (22)
  - HTTP (80)

---

# 1️⃣ Launch an EC2 Instance

| Setting | Value |
|---------|-------|
| AMI | Amazon Linux 2023 |
| Instance Type | t3.micro |
| Region | N. Virginia |
| VPC | Default |
| Inbound Rules | SSH (22), HTTP (80) |

---

# 2️⃣ Connect via SSH

```bash
ssh -i your-key.pem ec2-user@<PUBLIC-IP>
```

---

# 3️⃣ Update Packages

```bash
sudo dnf update -y
```

---

# 4️⃣ Install Apache

```bash
sudo dnf install -y httpd
```

Start and enable Apache:

```bash
sudo systemctl start httpd
sudo systemctl enable httpd
sudo systemctl status httpd
```

---

# 5️⃣ Create a Simple Web Page

```bash
echo "HELLO CLARUSWAY" | sudo tee /var/www/html/index.html
```

Restart Apache:

```bash
sudo systemctl restart httpd
```

---

# 6️⃣ Create an HTML Page

```html
<html>
<head>
    <title>My First Web Server</title>
</head>
<body>
    <h1>Hello Everyone from My First Web Server</h1>
</body>
</html>
```

---

# 7️⃣ Automate with User Data

```bash
#!/bin/bash
dnf update -y
dnf install -y httpd

DATE_TIME=$(date)

cat <<EOF >/var/www/html/index.html
<html>
<head>
<title>My First Web Server</title>
</head>
<body>
<h1>Hello Everyone from My First Web Server</h1>
<p>Created at: <b>$DATE_TIME</b></p>
</body>
</html>
EOF

systemctl enable httpd
systemctl start httpd
```

---

# 8️⃣ Test

Open:

```
http://<EC2-PUBLIC-IP>
```

or

```bash
curl http://<EC2-PUBLIC-IP>
```

---

## 📂 Project Structure

```
.
├── README.md
└── apache-web-server.png
```

---

## 🛠 Technologies

- AWS EC2
- Amazon Linux 2023
- Apache HTTP Server
- Bash
- HTML

---

## ⭐ Author

If this project helped you, consider giving it a ⭐ on GitHub.
