# Elastic Beanstalk Deployment Guide

This guide documents the deployment workflow used with the PHP application versions in this repository.

## Part 1 — Launch an Application

### 1. Prepare the source

Use the application bundle for version 1:

```text
mysampleapp-source-v1.zip
```

### 2. Create the Elastic Beanstalk application

In the AWS Console:

1. Open **Elastic Beanstalk**.
2. Click **Create Application**.
3. Keep **Web server environment**.
4. Application name: `MySampleApp`.
5. Environment name: `MySampleApp-env`.
6. Platform: **PHP**.
7. Platform branch: **PHP 8.3 running on 64bit Amazon Linux 2023**.
8. Platform version: **Recommended**.
9. Application code: **Upload your code** → **Local file**.
10. Version label: `mysampleapp-source-v1`.
11. Upload `mysampleapp-source-v1.zip`.
12. Select **High availability** for Presets.
13. Continue to the next step.

### 3. Service role and EC2 instance profile

For Service Role:

```text
Create and use new service role
```

Select the EC2 Key Pair.

For the EC2 instance profile, create/select:

```text
aws-elasticbeanstalk-ec2-role
```

The original lab specifies these policies:

- `AWSElasticBeanstalkWebTier`
- `AWSElasticBeanstalkWorkerTier`
- `AWSElasticBeanstalkMulticontainerDocker`

### 4. Capacity

Keep the optional networking, database and tag settings at their default values.

Under **Instances**:

```text
Root Volume Type: GP3
```

Under **Capacity**:

```text
Remove: t3.micro
Remove: t3.small
Select: t2.micro
```

Keep the other settings at their default values.

### 5. Create and verify

Keep update, monitoring and logging settings at their defaults.

Review the configuration and click **Submit**.

Wait for Elastic Beanstalk to create the environment.

Then:

- Open the **Application URL**.
- Show the running PHP application.
- Open the application and environment menus.
- Review **Configuration** and **Monitoring**.
- Review the AWS resources created by Elastic Beanstalk, including instances, load balancer, Auto Scaling resources, CloudFormation and S3 resources.
- Demonstrate that directly browsing to the public IP of the created instance does not provide the application in the same way as the Elastic Beanstalk URL; use this to explain the security-group/source configuration.

---

## Part 2 — Update the Application

The lab demonstrates three deployment policies:

1. All at Once
2. Rolling
3. Rolling with Additional Batch

### Step 1 — Update to v2: All at Once

Go to:

```text
Elastic Beanstalk
→ MySampleApp
→ MySampleApp-env
→ Upload and deploy
```

Use:

```text
Choose file : php-v2.zip
Version label: mysampleapp-source-v2
```

Deployment Preferences:

```text
Deployment policy : All at Once
Healthy threshold : OK
Ignore health check: False
```

Wait for the update to complete.

Open the Application URL and verify the updated application.

Then open:

```text
MySampleApp
→ Application versions
```

You should now be able to show the application versions for v1 and v2.

---

### Step 2 — Change Environment Capacity

Open:

```text
MySampleApp-env
→ Configuration
→ Capacity
→ Edit
```

Change the minimum number of instances:

```text
Instances Min: 2
Instances Max: 4
```

Save the configuration and allow the environment to update.

---

### Step 3 — Update to v3: Rolling

Open:

```text
MySampleApp-env
→ Upload and deploy
```

Use:

```text
Choose file : php-v3.zip
Version label: mysampleapp-source-v3
```

Deployment Preferences:

```text
Deployment policy : Rolling
Healthy threshold : OK
Ignore health check: False
```

Monitor **Events** and **Health** while the instances are updated one by one.

During the update, check the Application URL and demonstrate the transition from v2 to v3.

Then open:

```text
MySampleApp
→ Application versions
```

and show that three application versions are available.

---

### Step 4 — Update to v4: Rolling with Additional Batch

Open:

```text
MySampleApp-env
→ Upload and deploy
```

Use:

```text
Choose file : php-v4.zip
Version label: mysampleapp-source-v4
```

Deployment Preferences:

```text
Deployment policy : Rolling with Additional Batch
Healthy threshold : OK
Ignore health check: False
```

Monitor **Events** and **Health**.

Show that an additional instance is launched for the deployment.

During the update, check the Application URL and demonstrate the transition from v3 to v4.

After the deployment, show that one of the additional/old instances is terminated as the environment returns to its intended capacity.

---

## Part 3 — Terminate the Environment

### Step 1 — Terminate

Go to:

```text
Elastic Beanstalk
→ MySampleApp-env
→ Actions
→ Terminate environment
```

Confirm the environment name and click **Terminate**.

Wait for the environment to terminate and review **Recent events**.

### Step 2 — Restore

The lab then demonstrates restoring the terminated environment.

Go to:

```text
Elastic Beanstalk
→ Environments
→ MySampleApp-env
→ Actions
→ Restore
```

The original lab notes that a terminated environment remains visible for approximately one hour.

Verify that the environment is deployed and working again.

### Step 3 — Delete the Application

Go to:

```text
Elastic Beanstalk
→ Applications
→ MySampleApp
→ Actions
→ Delete application
```

Enter the application name to confirm deletion.

Wait for the deletion to complete and verify that both the environment and application have been removed.

---

## Deployment Strategy Summary

| Strategy | Version | Main demonstration |
|---|---|---|
| All at Once | v2 | Update the environment in one operation |
| Rolling | v3 | Update instances progressively |
| Rolling with Additional Batch | v4 | Add capacity during deployment to maintain availability |

The purpose of the lab is to compare how these deployment policies affect availability, instance replacement, capacity and application-version transitions.
