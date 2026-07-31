# ☁️ AWS CloudFormation - ALB with Auto Scaling Group

## 📖 Overview

This project demonstrates how to provision a highly available AWS infrastructure using CloudFormation.

Instead of manually creating AWS resources, the entire environment is deployed using Infrastructure as Code (IaC).

---

## 🏗️ AWS Services

- AWS CloudFormation
- Amazon EC2
- Launch Template
- Application Load Balancer
- Target Group
- Auto Scaling Group
- Amazon CloudWatch
- Security Groups

---

## 🚀 Features

- Infrastructure as Code
- Automatic EC2 Provisioning
- Load Balancing
- Auto Scaling
- Health Checks
- CloudWatch Monitoring

---

## 📂 Project Structure

```text
cloudformation-asg-alb
│
├── README.md
├── Cfn_Asg_LT.yaml
├── architecture-notes.md
└── deployment-checklist.md
```

---

## 🎯 Learning Objectives

- Deploy infrastructure using CloudFormation
- Automate EC2 provisioning
- Configure Launch Templates
- Create Auto Scaling Groups
- Configure Application Load Balancer
- Understand CloudFormation workflows

---

## ✅ Key Takeaways

- Infrastructure becomes repeatable.
- Deployments become faster.
- Manual configuration is minimized.
- Cloud resources remain consistent.

---

---

## 📚 AWS Services Reference

| Service | Purpose |
|---------|---------|
| AWS CloudFormation | Infrastructure as Code |
| Amazon EC2 | Virtual Servers |
| Launch Template | Instance Configuration |
| Auto Scaling Group | Automatic Scaling |
| Application Load Balancer | Traffic Distribution |
| Target Group | Backend Health Management |
| Amazon CloudWatch | Monitoring & Alarms |
| Security Groups | Network Security |

---

## 🧪 Validation Steps

- Verify CloudFormation stack status.
- Check Launch Template creation.
- Confirm Auto Scaling Group health.
- Access the Application Load Balancer DNS.
- Generate CPU load to validate scaling.
- Monitor CloudWatch alarms.