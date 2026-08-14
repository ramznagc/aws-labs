# Troubleshooting

## Overview

This document provides a basic troubleshooting checklist for connectivity and configuration problems when working with Amazon RDS MySQL.

## Connection Problems

### 1. RDS Instance Is Not Available

Check the RDS console and verify that the database instance is available.

### 2. Incorrect Endpoint

Verify that MySQL Workbench is using the correct RDS endpoint.

```text
<DB_INSTANCE_ENDPOINT>
```

### 3. Incorrect Port

MySQL commonly uses:

```text
3306
```

Verify that the connection is using the expected port.

### 4. Security Group

Check the inbound rules associated with the RDS instance.

The required MySQL traffic should be allowed from the appropriate source.

```text
Protocol: TCP
Port:     3306
Source:   Trusted Client
```

### 5. Incorrect Credentials

Verify:

* Username
* Password
* Database name

Never place the actual password in this repository.

### 6. Network Accessibility

Verify that the client can reach the RDS instance through the configured network path.

## Troubleshooting Flow

```text
Connection Failed
       │
       ▼
Check RDS Status
       │
       ▼
Check Endpoint
       │
       ▼
Check Port 3306
       │
       ▼
Check Security Group
       │
       ▼
Check Credentials
       │
       ▼
Check Network Configuration
```

## Security Reminder

Do not troubleshoot by committing credentials or sensitive infrastructure information to GitHub.

Use placeholders:

```text
<DB_USERNAME>
<DB_PASSWORD>
<DB_INSTANCE_ENDPOINT>
```

## Summary

A structured troubleshooting process helps identify whether a connection problem is caused by the database status, endpoint, port, network access, Security Group or credentials.
