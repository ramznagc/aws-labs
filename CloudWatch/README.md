# ☁️ Amazon CloudWatch — Monitoring, Alerting, Automation & Logging

<p align="center">
  <strong>EC2 Monitoring • CloudWatch Metrics • Dashboards • Alarms • SNS • EventBridge • Lambda • CloudWatch Agent • Logs</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/AWS-CloudWatch-orange?logo=amazon-aws&logoColor=white" alt="AWS CloudWatch">
  <img src="https://img.shields.io/badge/AWS-EC2-orange?logo=amazon-aws&logoColor=white" alt="AWS EC2">
  <img src="https://img.shields.io/badge/AWS-Lambda-orange?logo=amazon-aws&logoColor=white" alt="AWS Lambda">
  <img src="https://img.shields.io/badge/AWS-EventBridge-orange?logo=amazon-aws&logoColor=white" alt="AWS EventBridge">
  <img src="https://img.shields.io/badge/Type-Hands--on%20Lab-blue" alt="Hands-on Lab">
</p>

---

# 📖 Overview

**Amazon CloudWatch** is one of the core monitoring and observability services in AWS.

In a real production environment, it is not enough to simply create an EC2 instance and deploy an application.

We also need to know:

- Is the server healthy?
- Is CPU usage increasing?
- Is the application generating errors?
- Should an administrator be notified when something goes wrong?
- Can AWS automatically react to a problem?
- Can application logs be collected centrally?
- Can infrastructure tasks be automated according to a schedule?

This hands-on lab demonstrates how CloudWatch can be used to answer these questions.

Instead of looking at CloudWatch as a single dashboard, this lab approaches it as a complete workflow:

```text
                    AWS Infrastructure
                           │
                           ▼
                  Metrics + Application Logs
                           │
                           ▼
                    Amazon CloudWatch
                           │
            ┌──────────────┼──────────────┐
            │              │              │
            ▼              ▼              ▼
        Dashboard        Alarm           Logs
            │              │              │
            │              ▼              │
            │             SNS             │
            │              │              │
            │              ▼              │
            │            Email            │
            │                             │
            ▼                             ▼
       Visualization                Centralized Logs
```

The lab then extends monitoring into automation:

```text
                     EventBridge
                          │
                ┌─────────┴─────────┐
                │                   │
                ▼                   ▼
        Stop_Instance Lambda   Start_Instance Lambda
                │                   │
                ▼                   ▼
            EC2 Stop             EC2 Start
```

The overall concept is:

> **Monitor → Detect → Notify → Act → Automate → Log**

---

# 🎯 Learning Objectives

By completing this lab, I practiced how to:

- Launch an EC2 instance configured for CloudWatch monitoring
- Enable **CloudWatch Detailed Monitoring**
- Understand EC2 **CloudWatch Metrics**
- Create a CloudWatch Dashboard
- Visualize `CPUUtilization`
- Create a CloudWatch Alarm
- Configure an alarm threshold
- Integrate CloudWatch Alarms with Amazon SNS
- Trigger an EC2 action from an alarm
- Generate CPU load to test an alarm
- Create IAM permissions for Lambda
- Create Lambda functions with Python
- Use `boto3` to interact with EC2
- Start and stop EC2 instances programmatically
- Create scheduled EventBridge rules
- Automate EC2 lifecycle operations
- Install the CloudWatch Agent
- Collect Nginx access and error logs
- Understand CloudWatch Log Groups and Log Streams
- Connect monitoring, alerting, automation, and logging into one architecture

---

# 🏢 Real-World Scenario

Imagine that we are operating a small web application running on an Amazon EC2 instance.

The architecture starts simply:

```text
                    Internet
                       │
                       ▼
                     EC2
                       │
                       ▼
                     Nginx
```

The application is working, but we have a problem.

If CPU utilization becomes extremely high, nobody may notice until users start experiencing performance problems.

We therefore introduce monitoring:

```text
EC2
 │
 └── CPUUtilization
          │
          ▼
     CloudWatch
```

Then we introduce an alarm:

```text
CPUUtilization > 60%
          │
          ▼
   CloudWatch Alarm
```

But an alarm that nobody receives is not very useful.

So we integrate SNS:

```text
CloudWatch Alarm
       │
       ▼
      SNS
       │
       ▼
     Email
```

We can also automatically react:

```text
CloudWatch Alarm
       │
       ▼
   EC2 Stop Action
```

Now we have:

```text
             Production EC2
                   │
                   ▼
              CPU Metric
                   │
                   ▼
              CloudWatch
                   │
            ┌──────┴──────┐
            │             │
            ▼             ▼
        Dashboard       Alarm
                          │
                    ┌─────┴─────┐
                    │           │
                    ▼           ▼
                   SNS       EC2 Action
                    │
                    ▼
                  Email
```

The second part of the scenario is operational automation.

Suppose the development environment does not need to run continuously.

Instead of manually starting and stopping EC2 every day:

```text
Developer
   │
   ├── Start EC2
   │
   └── Stop EC2
```

we automate it:

```text
                  EventBridge
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
       Start Schedule       Stop Schedule
             │                   │
             ▼                   ▼
      Start Lambda          Stop Lambda
             │                   │
             ▼                   ▼
          EC2 Start            EC2 Stop
```

Finally, monitoring is extended to application logs:

```text
EC2
 │
 └── Nginx
      │
      ├── access.log
      └── error.log
              │
              ▼
       CloudWatch Agent
              │
              ▼
       CloudWatch Logs
```

This gives us a small but realistic observability and automation architecture.

---

# 🧠 How Amazon CloudWatch Works

CloudWatch can be understood through several major components.

```text
Amazon CloudWatch
│
├── Metrics
│
├── Dashboards
│
├── Alarms
│
├── Logs
│
└── Integrations
      │
      ├── SNS
      ├── EventBridge
      ├── Lambda
      └── EC2
```