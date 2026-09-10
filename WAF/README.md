# 🛡️ AWS WAF – Hands-on Lab

This lab focuses on protecting web applications using **AWS WAF (Web Application Firewall)** together with an **Application Load Balancer (ALB)**.

The infrastructure is deployed using **AWS CloudFormation**, allowing the required AWS resources to be created from a YAML template.

---

## 🎯 Learning Objectives

By completing this hands-on lab, I practiced:

- Creating an Application Load Balancer
- Creating EC2 web servers
- Creating Target Groups
- Configuring Security Groups
- Deploying infrastructure with CloudFormation
- Creating AWS WAF Web ACLs
- Associating a WAF Web ACL with an ALB
- Blocking traffic from a specific IP address
- Creating rate-based WAF rules
- Testing WAF protection against repeated requests

---

## 🏗️ Architecture

```text
                         🌍 Internet
                              │
                              ▼
                    ┌──────────────────┐
                    │  AWS WAF Web ACL │
                    │                  │
                    │ IP Blocking      │
                    │ Rate Limiting    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Application      │
                    │ Load Balancer    │
                    └────────┬─────────┘
                             │
                       Target Group
                             │
                 ┌───────────┴───────────┐
                 ▼                       ▼
          ┌─────────────┐         ┌─────────────┐
          │ EC2 Server  │         │ EC2 Server  │
          │ Apache HTTPD│         │ Apache HTTPD│
          └─────────────┘         └─────────────┘