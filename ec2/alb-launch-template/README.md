# ⚖️ Hands-on EC2 – Application Load Balancer (ALB) with Launch Template

## 📖 Overview

This hands-on demonstrates how to deploy a highly available web application using an **Application Load Balancer (ALB)** together with **Launch Templates** on AWS.

The lab covers creating security groups, launching EC2 instances from a launch template, configuring a target group, creating an Application Load Balancer, and testing health checks and failover behavior.

---

## 🎯 Learning Outcomes

After completing this lab, I can:

- Create and configure Security Groups
- Create and use Launch Templates
- Launch multiple EC2 instances
- Configure Target Groups
- Create an Application Load Balancer (ALB)
- Configure Listeners and Routing
- Perform Health Checks
- Understand Failover behavior
- Apply AWS security best practices

---

## 🏗️ AWS Services Used

- Amazon EC2
- Launch Templates
- Application Load Balancer (ALB)
- Target Groups
- Security Groups
- Amazon VPC

---

## 🔄 Architecture

```text
                 Internet
                     │
                     ▼
        ┌─────────────────────────┐
        │ Application Load Balancer │
        └────────────┬────────────┘
                     │
             Target Group
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
     EC2 Instance 1       EC2 Instance 2
        Apache               Apache
```

---

## 🛠️ Hands-on Steps

### 1️⃣ Create Security Groups

- EC2 Security Group
- ALB Security Group

### 2️⃣ Create Launch Template

- Amazon Linux 2023
- t3.micro
- User Data Script
- Apache Installation

### 3️⃣ Launch EC2 Instances

- Deploy multiple EC2 instances from the Launch Template

### 4️⃣ Create Target Group

- Register EC2 instances
- Configure Health Checks

### 5️⃣ Create Application Load Balancer

- Internet-facing ALB
- HTTP Listener
- Forward requests to Target Group

### 6️⃣ Verify Load Balancing

- Access the ALB DNS
- Observe requests distributed across EC2 instances

### 7️⃣ Test Health Checks

- Simulate an application failure
- Observe unhealthy target detection
- Verify automatic traffic failover

---

## 🔒 Security Best Practices

- Allow public HTTP access only through the ALB
- Restrict EC2 inbound traffic to the ALB Security Group
- Use Security Groups with least privilege
- Enable Health Checks
- Remove direct public access to backend instances

---

## 💡 Key Concepts

- Application Load Balancer (ALB)
- Launch Template
- Target Group
- Listener
- Health Check
- Failover
- Round Robin
- Security Group

---

## ✅ Key Takeaways

- Application Load Balancer improves availability and scalability.
- Health Checks automatically detect unhealthy instances.
- Traffic is routed only to healthy targets.
- Launch Templates simplify consistent EC2 deployments.
- Restricting EC2 access through the ALB increases security.

---

---

## 🚀 Common Use Cases

Application Load Balancers are commonly used in AWS environments for:

- Hosting highly available web applications
- Distributing traffic across multiple EC2 instances
- Performing health checks on application servers
- Routing traffic based on host names or URL paths
- Supporting Auto Scaling Groups
- Improving application fault tolerance

---

## 📚 References

- AWS EC2
- AWS Elastic Load Balancing
- AWS Launch Templates
- AWS Target Groups

---

---

## 📖 Key AWS Terms

| Service | Purpose |
|---------|---------|
| Application Load Balancer | Distributes HTTP/HTTPS traffic |
| Launch Template | Standardizes EC2 instance configuration |
| Target Group | Groups backend EC2 instances |
| Listener | Listens for incoming client requests |
| Health Check | Monitors target availability |
| Security Group | Controls inbound and outbound traffic |


⭐ Part of my AWS & Cloud Engineering hands-on documentation.