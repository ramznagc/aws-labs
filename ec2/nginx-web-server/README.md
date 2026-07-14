# 🚀 Amazon EC2 - Nginx Web Server

> Hands-on lab demonstrating how to deploy, configure, and automate an Nginx web server on an Amazon EC2 instance.

---

## 📖 Overview

In this lab, I launched an Amazon EC2 instance running Amazon Linux 2023, connected to it via SSH, installed and configured the Nginx web server, and automated the deployment using EC2 User Data.

This hands-on exercise demonstrates the fundamentals of web server deployment and basic infrastructure automation on AWS.

---

## 🎯 Learning Objectives

After completing this lab, I was able to:

- Launch an Amazon EC2 instance
- Connect to an EC2 instance using SSH
- Install and configure the Nginx Web Server
- Deploy a custom web page
- Create additional web content
- Automate server provisioning with EC2 User Data
- Verify the deployment using a web browser and curl

---

# 🛠️ Architecture

```text
Internet
      │
      ▼
Security Group
 (SSH 22 / HTTP 80)
      │
      ▼
Amazon EC2 (Amazon Linux 2023)
      │
      ▼
Nginx Web Server
      │
      ▼
Custom HTML Page
```

---

# Part 1 - Launch an EC2 Instance

Launch an EC2 instance with the following configuration:

| Setting | Value |
|---------|-------|
| AMI | Amazon Linux 2023 |
| Instance Type | t2.micro |
| Security Group | SSH (22), HTTP (80) |
| Key Pair | Your existing PEM file |

---

# Part 2 - Connect with SSH

Connect to the instance.

```bash
ssh -i your-key.pem ec2-user@PUBLIC-IP
```

---

# Part 3 - Install Nginx

Update packages.

```bash
sudo dnf update -y
```

Install Nginx.

```bash
sudo dnf install nginx -y
```

Start the service.

```bash
sudo systemctl start nginx
```

Enable automatic startup.

```bash
sudo systemctl enable nginx
```

Verify the service.

```bash
systemctl status nginx
```

---

# Part 4 - Deploy a Custom Web Page

Navigate to the web root directory.

```bash
cd /usr/share/nginx/html
```

Remove the default page.

```bash
sudo rm index.html
```

Download the sample website.

```bash
wget https://raw.githubusercontent.com/awsdevopsteam/route-53/master/index.html
wget https://raw.githubusercontent.com/awsdevopsteam/route-53/master/ken.jpg
```

Restart Nginx.

```bash
sudo systemctl restart nginx
```

Verify the website using the EC2 Public IP.

---

# Part 5 - Create an Additional Page

Create a second page.

```bash
echo "Second Page" > /usr/share/nginx/html/index_2.html
```

Access it from the browser.

```text
http://<Public-IP>/index_2.html
```

---

# Part 6 - Automate Deployment with User Data

Example User Data script:

```bash
#!/bin/bash
dnf update -y
dnf install nginx -y
systemctl start nginx
cd /usr/share/nginx/html
chmod -R 777 /usr/share/nginx/html
rm index.html
wget https://raw.githubusercontent.com/awsdevopsteam/route-53/master/index.html
wget https://raw.githubusercontent.com/awsdevopsteam/route-53/master/ken.jpg
systemctl restart nginx
systemctl enable nginx
```

Launch a new EC2 instance using this script and verify that the web server is automatically configured.

---

# ✅ Validation

- EC2 instance launched successfully
- SSH connection established
- Nginx installed and running
- Custom web page displayed
- User Data executed successfully
- Web server accessible from the browser
- Verified using `curl`

---

# 💡 AWS Best Practices

- Use Security Groups to restrict inbound traffic.
- Keep the operating system updated.
- Enable services that should start automatically.
- Use EC2 User Data to automate repetitive deployments.
- Avoid making unnecessary permission changes on production servers.

---

# 🧠 What I Learned

- Amazon EC2 fundamentals
- SSH connectivity
- Linux package management with DNF
- Nginx installation and configuration
- Basic web server deployment
- EC2 User Data automation
- Infrastructure automation basics

---

# 🚀 Next Lab

➡️ EC2 Launch Templates

---

# 📚 References

- AWS EC2 Documentation
- AWS User Data Documentation
- Nginx Documentation