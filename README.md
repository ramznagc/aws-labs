# ☁️ AWS Hands-on Labs

A practical learning portfolio documenting my hands-on work with **Amazon Web Services (AWS)**, cloud infrastructure, networking, security, monitoring, and automation.

This repository is organized by AWS service and real-world lab scenario. It includes implementation notes, architecture explanations, commands, configuration files, deployment steps, and cleanup guidance where available.

> **Learning approach:** build it, understand the architecture, test the behavior, troubleshoot, and clean up resources.

---

## 🧭 What I Have Practiced

### Core AWS Services

| Area | Hands-on topics | Labs |
|---|---|---|
| **Compute** | EC2 instances, SSH, Linux web servers, user data, Launch Templates, Auto Scaling Groups, AMIs, snapshots, EBS volumes | [EC2](ec2/) |
| **Networking** | VPCs, CIDR addressing, public/private subnets, route tables, Internet Gateway, NAT, bastion hosts, VPC peering, VPC endpoints, NACLs | [VPC](VPC/), [VPC-2](VPC-2/), [VPC-3](VPC-3/), [VPC-4](VPC-4/), [Networking](Networking/), [networking notes](networking/) |
| **Storage** | S3 object storage, static website hosting, bucket policies, versioning, lifecycle rules, cross-region replication, shared EFS, EBS management | [S3](S3/), [EFS](EFS/), [EC2 EBS volumes](ec2/ebs-volumes/) |
| **Identity & Security** | IAM, security groups, AWS WAF, Web ACLs, IP blocking, rate limiting, permissions for service integrations | [IAM](IAM/), [WAF](WAF/) |
| **Databases** | Amazon RDS and MySQL-related practice | [RDS](RDS/) |
| **DNS** | Route 53 and DNS-related infrastructure exercises | [Route 53](Route53/) |
| **Messaging** | Pub/sub notifications and decoupled messaging concepts with SNS and SQS | [SNS](SNS/), [SQS](SQS/) |
| **Monitoring & Operations** | CloudWatch metrics, dashboards, alarms, logs, SNS notifications, EventBridge schedules, Lambda-based EC2 operations | [CloudWatch](CloudWatch/) |
| **Infrastructure as Code** | YAML and CloudFormation templates; EC2, security groups, load balancers, Auto Scaling, WAF deployment | [CloudFormation](CloudFormation/) |
| **Application Deployment** | PHP application versions, Elastic Beanstalk environments, deployment strategies and application logging | [Elastic Beanstalk](ElasticBeanstalk/) |
| **Automation with Python** | Boto3 clients/resources, EC2 and S3 scripts, inventory-style scripts, AWS operations from Python | [Boto3](Boto3/) |
| **AWS CLI** | CLI installation/configuration, IAM, EC2, S3 and Systems Manager Parameter Store commands | [AWS CLI basics](CLI/aws-cli-basics/) |

---

## 🚀 Featured Hands-on Projects

### 1. Highly Available EC2 Web Application

Explore how Launch Templates, Target Groups, Application Load Balancers and Auto Scaling Groups work together to support web application availability and scaling.

- [ALB with Launch Template](ec2/alb-launch-template/)
- [Auto Scaling Group with Launch Template](ec2/asg-with-launch-template/)
- [Apache Web Server](ec2/apache-web-server/)
- [Nginx Web Server](ec2/nginx-web-server/)

### 2. AWS Networking and Private Connectivity

Practice designing networks that separate public-facing components from private workloads and control how traffic moves through AWS.

- [VPC fundamentals](VPC/)
- [Bastion Host and NAT](VPC-2/)
- [VPC Peering and VPC Endpoint](VPC-3/)
- [LAMP Stack, WordPress and NACLs](VPC-4/)

### 3. Storage, Backups and Recovery

Work with several AWS storage options and learn how storage configuration supports durability, sharing, recovery and web hosting.

- [S3 static website hosting and versioning](S3/s3-static-website-versioning/)
- [S3 lifecycle management and replication](S3/s3-lifecycle-replication/)
- [EFS shared by multiple EC2 instances](EFS/efs-01-multi-ec2/)
- [EBS volume management](ec2/ebs-volumes/)
- [Snapshots and AMIs](ec2/snapshots-and-amis/)

### 4. Monitoring, Alerting and Operations Automation

Connect monitoring signals to notifications and automated actions.

The CloudWatch lab documents practice with EC2 metrics, dashboards, alarms, SNS email notifications, Lambda functions, EventBridge schedules, and centralized Nginx logs through the CloudWatch Agent.

- [CloudWatch monitoring and automation](CloudWatch/)

### 5. Infrastructure as Code and Application Deployment

Use declarative templates to create AWS infrastructure, then explore application deployment and infrastructure protection.

- [First CloudFormation template](CloudFormation/first-cloudformation-template/)
- [CloudFormation ALB and Auto Scaling](CloudFormation/cloudformation-asg-alb/)
- [AWS WAF with CloudFormation](WAF/)
- [Elastic Beanstalk PHP application and deployment versions](ElasticBeanstalk/)

### 6. Python and Command-Line Automation

Use programmatic and command-line interfaces to work with AWS services.

- [AWS CLI installation and commands](CLI/aws-cli-basics/)
- [Boto3 hands-on scripts](Boto3/)
- [Cloud operations automation project](aws-cloudops-automation/)

The Cloud Operations Automation project includes a Python CLI, inventory modules for services such as EC2, IAM, Lambda, S3 and CloudWatch, and tests.

---

## 🧠 Skills Developed

Based on the labs and files in this repository, I have practiced:

- **Provisioning infrastructure:** launching and configuring EC2 instances and related networking resources.
- **Network design:** creating VPCs, subnetting, routing, private connectivity and controlled ingress/egress paths.
- **Storage administration:** working with EBS, EFS, S3 versioning, lifecycle management and replication.
- **Access control:** using IAM permissions and security groups, and exploring AWS WAF protections.
- **Load balancing and scaling:** building ALB, Launch Template and Auto Scaling configurations.
- **Infrastructure as Code:** describing AWS infrastructure with CloudFormation and YAML.
- **Observability:** measuring EC2 performance, configuring alarms, collecting logs and connecting notifications.
- **Operational automation:** scheduling actions with EventBridge and invoking AWS operations with Lambda and Boto3.
- **Application deployment:** practicing deployment versions and strategies with Elastic Beanstalk.
- **Troubleshooting and documentation:** recording procedures, architecture notes, checklists and cleanup steps.

These are skills practiced through repository labs; the presence of a lab does not by itself imply production experience or certification.

---

## 🌐 Networking Fundamentals

Alongside AWS-specific networking labs, the repository contains notes and examples for foundational topics.

| Topic | Materials |
|---|---|
| Network fundamentals | [Networking directory](Networking/) |
| IP addressing and subnetting | [Subnetting notes](networking/network-04-ip-subnetting.md) |
| Subnetting examples | [Subnetting examples](networking/network-04-ip-subnetting-examples.md) |
| VPC implementation | [VPC labs](VPC/) |

---

## 📁 Repository Structure

```text
aws-labs/
├── Boto3/                       # Python SDK exercises
├── CLI/                         # AWS CLI learning notes
├── CloudFormation/              # IaC templates and deployment labs
├── CloudWatch/                  # Monitoring, alerts, logs and automation
├── EFS/                         # Shared file systems
├── ElasticBeanstalk/             # Application deployment exercises
├── IAM/                         # Identity and access management
├── Lambda/                      # Serverless exercises
├── Networking/                  # Networking fundamentals
├── Organizations/                # AWS account organization notes
├── RDS/                         # Relational database exercises
├── Route53/                     # DNS and routing exercises
├── S3/                          # Object storage, hosting and replication
├── SNS/                         # Notifications
├── SQS/                         # Message queues
├── VPC/                         # VPC foundations
├── VPC-2/                       # NAT and bastion host
├── VPC-3/                       # Peering and endpoints
├── VPC-4/                       # LAMP/WordPress and NACLs
├── WAF/                         # Web application firewall
├── ec2/                         # EC2 scenarios and architecture labs
├── networking/                  # IP addressing and subnetting notes
└── aws-cloudops-automation/      # Python-based operations automation
```

Some service folders contain several focused labs, while others contain a main README and supporting notes or templates.

---

## 🗺️ Current Learning Roadmap

This repository is a work in progress. Areas to expand as I continue learning include:

- Deeper DNS, routing, VPN and hybrid-networking scenarios
- More automated testing and validation for infrastructure changes
- Improved least-privilege IAM policies and security hardening
- More reusable Infrastructure as Code components
- Expanded automated Cloud Operations workflows and documentation

The roadmap is a forward-looking plan, not a claim that every item is already completed.

---

## 💡 Notes for Running the Labs

- Most exercises require an AWS account, suitable IAM permissions and the relevant tools installed.
- Resource names, key pairs, AMI IDs, account-specific values and AWS Regions may need to be changed for your environment.
- Review security group rules and IAM policies before deployment.
- Check the expected costs of EC2, NAT Gateways, load balancers, storage and other billable services.
- Destroy only resources created for a lab and verify the plan before confirming.
- Never commit access keys, private keys, passwords, state files containing sensitive information, or other secrets.

---

## 🎯 Goal

My goal is to build practical cloud engineering skills by implementing AWS services, understanding their relationships, documenting what I learn, and progressively connecting individual labs into more complete operational scenarios.

**Learn by building. Understand by testing. Improve by documenting.**

---

*Repository: [ramznagc/aws-labs](https://github.com/ramznagc/aws-labs)*
