# RDS MySQL Configuration

## Overview

This document describes the main configuration steps for the Amazon RDS MySQL database used in this project.

The purpose of this document is to explain how the RDS database was configured and prepared for client connections.

## Database Engine

The database engine used in this project is:

```text
MySQL
```

Amazon RDS provides the managed database infrastructure while AWS manages the underlying database environment.

## Basic Configuration

The RDS database requires several configuration values.

| Setting                | Value                      |
| ---------------------- | -------------------------- |
| Engine                 | MySQL                      |
| DB Instance Identifier | `<DB_INSTANCE_IDENTIFIER>` |
| Database Name          | `<DATABASE_NAME>`          |
| Master Username        | `<DB_USERNAME>`            |
| Port                   | `3306`                     |

Sensitive information such as passwords should never be stored in this repository.

## Network Connectivity

The database client connects to the RDS instance using the MySQL protocol.

```text
MySQL Workbench
       │
       │ TCP 3306
       ▼
Amazon RDS MySQL
```

The standard MySQL port is:

```text
3306
```

## Security Group

The RDS instance uses a Security Group to control network traffic.

Example MySQL inbound rule:

```text
Type:     MySQL/Aurora
Protocol: TCP
Port:     3306
Source:   Trusted Client IP
```

For production environments, database access should be restricted to the smallest practical network scope.

Avoid unrestricted database access whenever possible.

## RDS Endpoint

The RDS instance provides an endpoint that database clients use for connectivity.

Example:

```text
<DB_INSTANCE_ENDPOINT>
```

The endpoint should be used by the database client when establishing a connection.

## Configuration Checklist

* [ ] Create the RDS MySQL instance
* [ ] Configure the DB instance identifier
* [ ] Configure the database credentials
* [ ] Configure networking
* [ ] Configure the Security Group
* [ ] Allow TCP port `3306` from the required source
* [ ] Obtain the RDS endpoint
* [ ] Test database connectivity

## Security Notes

Never commit credentials to GitHub.

Do not store:

```text
<DB_PASSWORD>
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
Private Keys
```

Use placeholders instead:

```text
<DB_USERNAME>
<DB_PASSWORD>
<DB_INSTANCE_ENDPOINT>
```

## Summary

The RDS configuration provides the managed MySQL database required for the next stage of the project: connecting through MySQL Workbench and performing SQL operations.
