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

---

---

## 🛡️ AWS Best Practices

- Use Launch Templates instead of Launch Configurations.
- Configure Health Checks for all targets.
- Keep desired capacity based on application requirements.
- Avoid aggressive scaling thresholds.
- Monitor infrastructure using Amazon CloudWatch.
- Distribute instances across multiple Availability Zones.

---

---

## 📚 AWS Services Reference

| Service | Purpose |
|---------|---------|
| Amazon EC2 | Virtual machines |
| Launch Template | EC2 configuration template |
| Auto Scaling Group | Automatic instance scaling |
| Application Load Balancer | Traffic distribution |
| Target Group | Backend instance management |
| Amazon CloudWatch | Monitoring and alarms |
| Security Groups | Network access control |

---

---

# 🔍 Validation Checklist

After completing this hands-on, verify the following:

- [ ] Launch Template created successfully
- [ ] Target Group reports healthy targets
- [ ] Application Load Balancer is routing traffic correctly
- [ ] Auto Scaling Group launches the desired number of instances
- [ ] Scale-Out policy is triggered when CPU utilization increases
- [ ] Scale-In policy removes unnecessary instances
- [ ] CloudWatch alarms change state correctly
- [ ] Application remains available during scaling events