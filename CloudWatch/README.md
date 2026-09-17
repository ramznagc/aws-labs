# ☁️ Amazon CloudWatch — Production Monitoring & Automation Lab

<p align="center">
  <strong>Monitoring • Metrics • Dashboards • Alarms • SNS • EventBridge • Lambda • Logs</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/AWS-CloudWatch-orange?logo=amazon-aws&logoColor=white" alt="AWS CloudWatch">
  <img src="https://img.shields.io/badge/AWS-EC2-orange?logo=amazon-aws&logoColor=white" alt="AWS EC2">
  <img src="https://img.shields.io/badge/AWS-Lambda-orange?logo=amazon-aws&logoColor=white" alt="AWS Lambda">
  <img src="https://img.shields.io/badge/AWS-EventBridge-orange?logo=amazon-aws&logoColor=white" alt="AWS EventBridge">
  <img src="https://img.shields.io/badge/Status-Completed-success" alt="Completed">
</p>

> A realistic hands-on AWS monitoring and automation scenario demonstrating how CloudWatch can be used to monitor infrastructure, detect problems, notify administrators, automate EC2 operations, and centralize application logs.

---

# 📖 Table of Contents

- [🏢 Real-World Scenario](#-real-world-scenario)
- [🎯 Business Requirements](#-business-requirements)
- [🧠 Why CloudWatch?](#-why-cloudwatch)
- [🏗️ Architecture](#️-architecture)
- [🔄 How the System Works](#-how-the-system-works)
- [📊 CloudWatch Metrics](#-cloudwatch-metrics)
- [📈 CloudWatch Dashboard](#-cloudwatch-dashboard)
- [🚨 CloudWatch Alarms](#-cloudwatch-alarms)
- [🔔 SNS Notifications](#-sns-notifications)
- [⚡ EventBridge Automation](#-eventbridge-automation)
- [λ Lambda EC2 Automation](#-lambda-ec2-automation)
- [📝 CloudWatch Logs](#-cloudwatch-logs)
- [⚙️ CloudWatch Agent](#️-cloudwatch-agent)
- [🔐 IAM Permissions](#-iam-permissions)
- [🧪 Testing & Validation](#-testing--validation)
- [📋 Lab Checklist](#-lab-checklist)
- [🧹 Cleanup](#-cleanup)
- [🧠 Lessons Learned](#-lessons-learned)
- [⭐ Final Architecture](#-final-architecture)

---

# 🏢 Real-World Scenario

Imagine a company called:

## **ClarusWeb**

ClarusWeb runs a web application on AWS.

The application is hosted on an **Amazon EC2 instance** and uses **Nginx** as its web server.

The infrastructure currently looks like:

```text
                    Internet
                        │
                        ▼
                     Nginx
                        │
                        ▼
                   Amazon EC2