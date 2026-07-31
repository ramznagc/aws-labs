# 🏗️ Architecture Overview

## Components

- AWS CloudFormation
- Launch Template
- Auto Scaling Group
- Amazon EC2
- Target Group
- Application Load Balancer
- Amazon CloudWatch

---

## Deployment Flow

CloudFormation

↓

Launch Template

↓

Auto Scaling Group

↓

EC2 Instances

↓

Target Group

↓

Application Load Balancer

↓

Users

---

## Benefits

- Infrastructure as Code
- High Availability
- Automatic Scaling
- Easy Resource Management
- Repeatable Deployments

---

## Best Practices

- Use Launch Templates instead of Launch Configurations.
- Enable Health Checks.
- Use CloudWatch monitoring.
- Deploy resources across multiple Availability Zones.