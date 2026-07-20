# ☁️ AWS CloudFormation - First Infrastructure as Code Lab

> A hands-on lab introducing YAML fundamentals and AWS CloudFormation by creating an EC2 instance and Security Group using Infrastructure as Code.

---

## 📖 Overview

In this hands-on lab, I practiced **YAML fundamentals** and created my first **AWS CloudFormation template**.

Instead of manually creating resources through the AWS Management Console, I defined AWS infrastructure using code.

The CloudFormation template provisions:

- 🖥️ An Amazon EC2 instance
- 🔐 An EC2 Security Group
- 🔑 SSH access on port `22`
- 🌐 HTTP access on port `80`
- 🏷️ Resource tagging

This lab was my introduction to **Infrastructure as Code (IaC)** using AWS CloudFormation.

---

## 🎯 Learning Objectives

After completing this lab, I was able to:

- Understand basic YAML syntax and indentation
- Work with YAML key-value pairs and lists
- Understand nested YAML structures
- Create an AWS CloudFormation template
- Define AWS resources using YAML
- Use CloudFormation intrinsic functions such as `!Ref`
- Provision an EC2 instance and Security Group as code
- Understand the fundamentals of Infrastructure as Code

---

## 📁 Lab Structure

```text
first-cloudformation-template/
├── README.md
├── example-yaml.yaml
└── first-cfn-template.yaml
```

### `example-yaml.yaml`

Contains examples of YAML fundamentals used to understand the syntax before working with CloudFormation.

Topics include:

- Key-value pairs
- Lists
- Nested structures
- Comments
- Multi-line values

### `first-cfn-template.yaml`

Contains the AWS CloudFormation template used to define and provision AWS infrastructure.

---

## 🏗️ Architecture

```text
       AWS CloudFormation
              │
              ▼
      CloudFormation Stack
              │
       ┌──────┴──────┐
       │             │
       ▼             ▼
  EC2 Instance   Security Group
                       │
                  ┌────┴────┐
                  │         │
               SSH:22    HTTP:80
```

---

## 🧱 AWS Resources

The CloudFormation template creates two main resources:

### 🖥️ Amazon EC2 Instance

The EC2 instance is defined using:

```yaml
Type: AWS::EC2::Instance
```

The instance configuration includes:

- Amazon Machine Image (AMI)
- EC2 instance type
- Key pair
- Security Group
- Resource tags

---

### 🔐 Security Group

The Security Group is defined using:

```yaml
Type: AWS::EC2::SecurityGroup
```

It allows inbound traffic for:

| Protocol | Port | Purpose |
|---|---:|---|
| TCP | 22 | SSH Access |
| TCP | 80 | HTTP Web Traffic |

---

## 🔗 Resource References

CloudFormation resources can reference each other using intrinsic functions.

Example:

```yaml
SecurityGroups:
  - !Ref MyCfnSG
```

The `!Ref` function allows the EC2 instance to reference the Security Group created within the same CloudFormation stack.

---

## 🚀 Deployment Workflow

```text
Write YAML Template
        ↓
Create CloudFormation Stack
        ↓
CloudFormation Reads Template
        ↓
AWS Resources Are Provisioned
        ↓
EC2 Instance + Security Group
        ↓
Verify Resources
        ↓
Delete Stack
```

---

## 🔐 Security Note

For learning purposes, the template may allow SSH access from:

```text
0.0.0.0/0
```

This allows connections from any IP address.

In production environments, SSH access should be restricted to trusted IP addresses or network ranges.

The **AMI ID** and **Key Pair name** may also need to be changed depending on the AWS account and region where the template is deployed.

---

## 🛠️ Technologies Used

- AWS CloudFormation
- Amazon EC2
- AWS Security Groups
- YAML
- Infrastructure as Code (IaC)
- Git & GitHub

---

## 🧠 What I Learned

Through this hands-on lab, I strengthened my understanding of:

- YAML fundamentals
- Infrastructure as Code
- AWS CloudFormation templates
- Automated AWS resource provisioning
- EC2 resource definitions
- Security Group configuration
- CloudFormation resource references

This lab helped me understand how cloud infrastructure can be defined, deployed, and managed consistently using code.

---

## 🚀 Next Steps

- Add CloudFormation Parameters
- Add CloudFormation Outputs
- Use dynamic AMI references
- Improve Security Group configuration
- Add EC2 User Data
- Automate web server deployment

---

⭐ This lab is part of my ongoing **AWS, Cloud & DevOps learning journey**.