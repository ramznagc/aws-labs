# 🌐 Route 53 – Hands-on Lab 01

Welcome to my **Amazon Route 53 Hands-on Lab**.

This lab focuses on the fundamentals of **DNS, Route 53 record sets, domain name routing, and integrating Route 53 with AWS services such as EC2, S3 Static Website Hosting, and ELB**.

---

## 🎯 Learning Objectives

By completing this hands-on lab, you will learn how to:

- Create and manage Route 53 record sets
- Understand Route 53 Public Hosted Zones
- Understand **SOA** and **NS** records
- Create **A records**
- Create **CNAME records**
- Create **Alias records**
- Route traffic to EC2 instances
- Route traffic to an S3 Static Website
- Route traffic to an ELB
- Verify DNS resolution using `nslookup`
- Understand basic domain name routing

---

## 🗺️ Lab Outline

```text
Route 53 – Hands-on Lab 01
│
├── Part 1 – Preparation
│   ├── Security Group
│   ├── EC2 Instance 1
│   ├── EC2 Instance 2
│   ├── S3 Static Website
│   └── Auto Scaling + ALB
│
├── Part 2 – Route 53 Fundamentals
│   ├── Public Hosted Zone
│   ├── SOA Record
│   ├── NS Records
│   └── Private Hosted Zone
│
├── Part 3 – A Records
│   ├── www → EC2 Instance
│   ├── info → EC2 Instance
│   └── Multiple IP Addresses
│
├── Part 4 – CNAME Records
│   └── Domain → Another Domain
│
└── Part 5 – Alias Records
    ├── Route 53 → S3
    └── Route 53 → ELB