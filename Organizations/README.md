# ☁️ AWS Organizations & IAM Identity Center

Hands-on lab focused on **AWS Organizations, multi-account management, security policies, and centralized access control**.

## 🎯 What I Practiced

- AWS Organizations & multi-account management
- Organizational Units (OU)
- Service Control Policies (SCP)
- EC2 instance type restrictions
- AWS Region restrictions
- Tag Policies
- IAM Identity Center
- Permission Sets & user assignments

## 🏗️ Architecture

```text
AWS Organization
│
├── Root
│   └── TeamA
│       └── sandbox1
│
├── SCP
│   ├── EC2 Restrictions
│   └── Region Restrictions
│
├── Tag Policies
│
└── IAM Identity Center
    └── Permission Sets
```

## 🛡️ Key Concepts

| Feature | Purpose |
|---|---|
| AWS Organizations | Multi-account management |
| OU | Account organization |
| SCP | Centralized permission control |
| Tag Policy | Resource tagging governance |
| IAM Identity Center | Centralized user access |
| Permission Sets | Role-based access |

## ⭐ Key Takeaway

This lab helped me understand how AWS Organizations can be used to manage **multiple AWS accounts, enforce security policies, standardize resources, and control user access centrally**.

> **Learn → Build → Test → Document**