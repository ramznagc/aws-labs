# ☁️ AWS IAM Hands-on Lab

> A beginner-friendly hands-on lab for learning the fundamentals of AWS Identity and Access Management (IAM).

---

## 📖 Overview

AWS Identity and Access Management (IAM) enables you to securely manage access to AWS resources.

In this hands-on lab, you will learn how to create and manage IAM users, groups, policies, and roles by following AWS security best practices.

---

## 🎯 Learning Objectives

After completing this lab, you will be able to:

- Understand the difference between the Root User and IAM Users
- Create and manage IAM users
- Configure IAM user settings
- Create IAM groups
- Attach AWS managed policies
- Troubleshoot IAM credentials
- Create IAM roles
- Attach IAM roles to EC2 instances
- Apply AWS security best practices

---

## 📚 Table of Contents

1. Creating IAM Users
2. Creating IAM Groups
3. Troubleshooting Credentials
4. Creating IAM Roles
5. Attaching IAM Roles to EC2
6. AWS Best Practices
7. Summary

---

# Part 1 – Creating IAM Users

## Step 1 – Sign in as the Root User

- Sign in using your AWS Root Account.
- Use the Root User only for initial account setup.

> ⚠️ **Important:** AWS recommends using an IAM user instead of the Root User for everyday tasks.

---

## Step 2 – Create an Administrator IAM User

Navigate to:

```
IAM → Users → Create User
```

Attach the following AWS managed policy:

```
AdministratorAccess
```

This IAM user will be used for daily AWS administration.

---

## Step 3 – Configure Billing Access

Enable:

```
IAM User and Role Access to Billing Information
```

Then:

- Sign out
- Sign in using the new IAM user
- Verify access to Billing and IAM services

---

# Part 2 – Creating IAM Groups

## Database Group

Create a group named:

```
Database
```

Attach the following policy:

- AmazonRDSFullAccess

Assign database users to this group.

---

## Developer Group

Create a group named:

```
Developer
```

Attach the following policies:

- AmazonEC2FullAccess
- AmazonS3FullAccess

Assign developer users to this group.

---

# Part 3 – Troubleshooting Credentials

Practice the following tasks:

- Reset Console Password
- Deactivate Access Keys
- Delete Access Keys
- Create New Access Keys

Understand the purpose of:

- Console Password
- Access Key ID
- Secret Access Key

---

# Part 4 – Creating IAM Roles

Create an IAM Role using the following configuration:

| Setting | Value |
|---------|-------|
| Trusted Entity | AWS Service |
| Service | EC2 |
| Permission | AmazonS3FullAccess |
| Role Name | FirstRoleS3Full |

---

## Launch an EC2 Instance Without an IAM Role

Launch an Amazon Linux EC2 instance without attaching any IAM role.

### Expected Result

❌ The EC2 instance cannot access Amazon S3 objects.

---

## Launch an EC2 Instance With an IAM Role

Attach:

```
FirstRoleS3Full
```

Launch the same EC2 instance again.

### Expected Result

✅ The EC2 instance successfully downloads files from Amazon S3 using the attached IAM Role.

---

# 💡 AWS Best Practices

- Never use the Root User for daily operations.
- Follow the Principle of Least Privilege.
- Use IAM Groups to simplify permission management.
- Prefer IAM Roles over Access Keys for AWS services.
- Rotate credentials regularly.
- Enable Multi-Factor Authentication (MFA).

---

# 🧠 What I Learned

After completing this lab, I gained hands-on experience with:

- ✅ IAM Users
- ✅ IAM Groups
- ✅ AWS Managed Policies
- ✅ IAM Roles
- ✅ EC2 Role Attachment
- ✅ Credential Management
- ✅ AWS Security Best Practices

---

# 🚀 Next Lab

➡️ Amazon EC2

---

# 📚 References

- https://docs.aws.amazon.com/IAM/
- https://aws.amazon.com/iam/
- https://docs.aws.amazon.com/wellarchitected/
