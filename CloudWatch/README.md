# ☁️ CloudWatch CW-01 — Hands-on Lab

<p align="center">
  <strong>Amazon CloudWatch • Dashboard • Alarms • EventBridge • Lambda • CloudWatch Agent</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/AWS-CloudWatch-orange?logo=amazon-aws&logoColor=white" alt="AWS CloudWatch">
  <img src="https://img.shields.io/badge/Type-Hands--on%20Lab-blue" alt="Hands-on Lab">
  <img src="https://img.shields.io/badge/Status-Completed-success" alt="Completed">
</p>

> **Goal:** Build practical experience with AWS monitoring, alarms, event-driven automation, and centralized logging using Amazon CloudWatch and related AWS services.

---

## 🧭 Navigation

- [🎯 Learning Outcomes](#-learning-outcomes)
- [🏗️ Lab Architecture](#️-lab-architecture)
- [📋 Lab Outline](#-lab-outline)
- [🖥️ Part 1 — EC2 Preparation](#️-part-1--ec2-preparation)
- [📊 Part 2 — CloudWatch Dashboard](#-part-2--cloudwatch-dashboard)
- [🚨 Part 3 — CloudWatch Alarm](#-part-3--cloudwatch-alarm)
- [⚡ Part 4 — EventBridge + Lambda](#-part-4--eventbridge--lambda)
- [📝 Part 5 — CloudWatch Agent Logging](#-part-5--cloudwatch-agent-logging)
- [🧪 Verification Checklist](#-verification-checklist)
- [🧹 Cleanup](#-cleanup)
- [🧠 Key Takeaways](#-key-takeaways)

---

## 🎯 Learning Outcomes

By completing this hands-on lab, I practiced how to:

- Create a **CloudWatch Dashboard**
- Monitor **EC2 CPU utilization**
- Create and configure a **CloudWatch Alarm**
- Send alarm notifications through **Amazon SNS**
- Configure an EC2 stop action from a CloudWatch Alarm
- Create scheduled **Amazon EventBridge** rules
- Use **AWS Lambda** to start and stop EC2 instances
- Configure the **Amazon CloudWatch Agent**
- Send Nginx access and error logs to **CloudWatch Logs**
- Monitor and automate AWS resources using multiple services together

---

## 🏗️ Lab Architecture

```text
                         AWS CloudWatch
                              │
             ┌────────────────┼─────────────────┐
             │                │                 │
             ▼                ▼                 ▼
         Dashboard          Alarm          CloudWatch Logs
             │                │                 ▲
             │                ▼                 │
             │               SNS                │
             │                │                 │
             ▼                ▼                 │
        EC2 Metrics      Email Notification     │
                              │                 │
                              ▼                 │
                         Stop Instance          │
                                                │
EC2 ──► Nginx ──► CloudWatch Agent ────────────┘