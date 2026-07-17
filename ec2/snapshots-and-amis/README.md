# 📸 Amazon EC2 - Snapshots & Amazon Machine Images (AMI)

> Hands-on lab demonstrating how to create EBS snapshots, build Amazon Machine Images (AMIs), launch EC2 instances from AMIs, and automate backups using AWS Data Lifecycle Manager.

---

# 📖 Overview

Amazon EBS Snapshots and Amazon Machine Images (AMIs) are essential services for backup, disaster recovery, and rapid infrastructure deployment.

In this lab, I created snapshots from EBS volumes, generated custom AMIs, launched new EC2 instances from those AMIs, and explored automated snapshot management using AWS Data Lifecycle Manager.

---

# 🎯 Learning Objectives

After completing this lab, I was able to:

- Create EBS snapshots
- Create Amazon Machine Images (AMI)
- Launch EC2 instances from custom AMIs
- Understand the difference between Snapshots and AMIs
- Configure AWS Data Lifecycle Manager (DLM)
- Share and publish AMIs

---

# 🏗️ Architecture

```text
Amazon EC2 Instance
        │
        ▼
   EBS Volume
        │
        ▼
   EBS Snapshot
        │
        ▼
 Amazon Machine Image (AMI)
        │
        ▼
 Launch New EC2 Instance
```

---

# Part 1 - Create an EBS Snapshot

Launch an EC2 instance with Nginx installed.

Create an EBS Snapshot from the instance.

Configuration:

| Resource | Value |
|----------|-------|
| Resource Type | Instance |
| Snapshot Name | FirstSnapshotNginx |

Verify that the snapshot is successfully created.

---

# Part 2 - Create an AMI from the Snapshot

From the created snapshot:

**Actions → Create Image**

Configuration:

| Setting | Value |
|---------|-------|
| Name | FirstAMINginx |
| Description | FirstAMINginx |

Wait until the AMI status becomes **Available**.

---

# Part 3 - Launch an EC2 Instance from the AMI

Navigate to:

**EC2 → AMIs**

Select your custom AMI.

Launch a new EC2 instance.

Verify:

- Instance is running
- Nginx is installed
- Website is accessible using the Public IP

---

# Part 4 - Create an AMI Using EC2 Actions

Instead of creating a snapshot manually:

EC2 Instance

→ Actions

→ Image and Templates

→ Create Image

AWS automatically creates the required snapshot in the background.

---

# Part 5 - AWS Data Lifecycle Manager (DLM)

Create an automated snapshot policy.

Configuration example:

| Setting | Value |
|---------|-------|
| Policy Type | EBS Snapshot Policy |
| Resource Type | Instance |
| Frequency | Daily |
| Retention | 5 Snapshots |
| Schedule | Every 24 Hours |

Apply the policy using instance tags.

---

# Part 6 - Share an AMI

Select the AMI.

Navigate to:

**Permissions → Make Public**

This allows other AWS accounts to use your custom AMI.

> **Note:** Public AMIs should only be shared after removing sensitive information.

---

# 🔄 Snapshot vs AMI

| Snapshot | AMI |
|-----------|-----|
| Stores EBS volume data | Stores a complete machine image |
| Used for backups | Used to launch EC2 instances |
| Can create an AMI | Can contain one or more snapshots |
| Storage-level backup | Full deployment template |

---

# 💻 AWS Services Used

- Amazon EC2
- Amazon EBS
- Amazon Machine Image (AMI)
- Amazon Data Lifecycle Manager (DLM)

---

# ✅ Validation Checklist

- EBS Snapshot created
- Custom AMI created
- New EC2 launched successfully
- Nginx application preserved
- Snapshot automation configured
- AMI sharing completed

---

# 💡 AWS Best Practices

- Take snapshots before modifying production volumes.
- Use DLM to automate backups.
- Tag EC2 resources consistently.
- Delete unused snapshots and AMIs to reduce costs.
- Never publish sensitive AMIs.

---

# 🧠 What I Learned

- Amazon EBS Snapshots
- Amazon Machine Images (AMI)
- Backup and recovery strategies
- Infrastructure cloning
- Automated snapshot management
- Data Lifecycle Manager

---

# 🚀 Next Lab

➡️ Amazon VPC Fundamentals