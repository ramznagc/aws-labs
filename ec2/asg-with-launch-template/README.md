# 🚀 Hands-on EC2 - Auto Scaling Group (ASG) with Launch Template

## 📖 Overview

This hands-on demonstrates how to build a highly available and scalable AWS infrastructure by integrating an Application Load Balancer with an Auto Scaling Group using a Launch Template.

---

## 🎯 Learning Outcomes

- Create a Launch Template
- Configure an Application Load Balancer
- Create a Target Group
- Configure an Auto Scaling Group
- Configure CloudWatch Alarms
- Create Scaling Policies
- Test automatic scaling
- Understand High Availability

---

## ☁️ AWS Services

- Amazon EC2
- Application Load Balancer
- Target Group
- Launch Template
- Auto Scaling Group
- Amazon CloudWatch

---

## 🏗 Architecture

Internet

↓

Application Load Balancer

↓

Target Group

↓

Auto Scaling Group

↓

EC2 Instances

---

## Auto Scaling Configuration

Desired Capacity : 2

Minimum Capacity : 1

Maximum Capacity : 4

---

## Scaling Policies

### Scale Out

CPU > 60%

→ Add 1 EC2 Instance

### Scale In

CPU < 30%

→ Remove 1 EC2 Instance

---

## CloudWatch

CloudWatch monitors EC2 metrics and automatically triggers scaling policies based on CPU utilization.

---

## Key Concepts

- High Availability
- Elastic Scaling
- Fault Tolerance
- Cloud Monitoring
- Launch Template
- Health Checks

---

## Key Takeaways

- Automatically scales EC2 instances.
- Improves application availability.
- Optimizes infrastructure costs.
- Uses CloudWatch for monitoring.
- Supports highly available architectures.

---

---

## 🧪 Testing Scenarios

After deployment, validate the following:

- Verify healthy targets in the Target Group.
- Stop one EC2 instance and confirm Auto Scaling launches a replacement.
- Generate CPU load using the `stress` tool.
- Verify Scale-Out policy execution.
- Stop the stress test and verify Scale-In policy execution.
- Monitor CloudWatch metrics during scaling events.