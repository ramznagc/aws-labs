# ☁️ AWS IAM Hands-on Lab

> A beginner-friendly hands-on lab for learning the fundamentals of AWS Identity and Access Management (IAM).

---

## 📖 Overview

AWS Identity and Access Management (IAM) is a service that helps you securely control access to AWS resources.

In this lab, I practiced creating IAM users, groups, policies, and roles while following AWS security best practices.

---

## 🎯 Learning Objectives

After completing this lab, I was able to:

- Understand the difference between the Root User and IAM Users
- Create IAM Users
- Create IAM Groups
- Attach AWS Managed Policies
- Create IAM Roles
- Attach IAM Roles to EC2
- Troubleshoot IAM credentials
- Apply AWS security best practices

---

## 📚 Lab Sections

1. Creating IAM Users
2. Creating IAM Groups
3. Troubleshooting Credentials
4. Creating IAM Roles
5. Attaching IAM Roles to EC2

---

# Part 1 – Creating IAM Users

- Sign in using the AWS Root Account.
- Create an IAM User.
- Attach the **AdministratorAccess** policy.
- Configure Billing access for the IAM User.

> 💡 **Best Practice:** Never use the Root User for daily administrative tasks.

---

# Part 2 – Creating IAM Groups

Create the following groups:

### Database

Policy:

- AmazonRDSFullAccess

### Developer

Policies:

- AmazonEC2FullAccess
- AmazonS3FullAccess

Assign users to the appropriate groups.

---

# Part 3 – Troubleshooting Credentials

Practice:

- Reset Console Password
- Delete Access Keys
- Create New Access Keys

---

# Part 4 – Creating IAM Roles

Create an IAM Role.

| Setting | Value |
|---------|-------|
| Trusted Entity | AWS Service |
| Service | EC2 |
| Permission | AmazonS3FullAccess |
| Role Name | FirstRoleS3Full |

---

# Part 5 – Attach IAM Role to EC2

Launch an EC2 instance:

- Without an IAM Role
- With the **FirstRoleS3Full** IAM Role

Observe the difference in Amazon S3 access.

---

# 💡 AWS Best Practices

- Never use the Root User for daily work.
- Use IAM Roles instead of Access Keys.
- Follow the Principle of Least Privilege.
- Enable Multi-Factor Authentication (MFA).
- Rotate credentials regularly.

---

# 🧠 What I Learned

- ✅ IAM Users
- ✅ IAM Groups
- ✅ IAM Policies
- ✅ IAM Roles
- ✅ EC2 Role Attachment
- ✅ AWS Security Best Practices

---

# 🚀 Next Lab

➡️ Amazon EC2
