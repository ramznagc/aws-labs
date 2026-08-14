# MySQL Workbench Connection

## Overview

MySQL Workbench can be used as a graphical client for connecting to an Amazon RDS MySQL database.

This document describes the connection information and steps required to connect MySQL Workbench to the RDS instance.

## Required Connection Information

The following information is required:

| Field           | Value                    |
| --------------- | ------------------------ |
| Connection Name | `AWS RDS MySQL`          |
| Hostname        | `<DB_INSTANCE_ENDPOINT>` |
| Port            | `3306`                   |
| Username        | `<DB_USERNAME>`          |
| Password        | `<DB_PASSWORD>`          |

The actual password must not be committed to GitHub.

## Create a New Connection

Open MySQL Workbench and create a new MySQL connection.

Use the following configuration:

```text
Connection Name:
AWS RDS MySQL

Hostname:
<DB_INSTANCE_ENDPOINT>

Port:
3306

Username:
<DB_USERNAME>
```

Enter the password securely when requested.

## Connection Flow

```text
MySQL Workbench
       │
       │ Hostname + Port
       ▼
Security Group
       │
       │ TCP 3306
       ▼
Amazon RDS MySQL
```

## Test the Connection

After entering the connection information, use the connection test option in MySQL Workbench.

A successful connection confirms that:

* The RDS instance is available
* The endpoint is correct
* The port is reachable
* The Security Group allows the connection
* The credentials are valid

## Troubleshooting Checklist

If the connection fails, verify:

1. RDS instance status
2. RDS endpoint
3. MySQL port `3306`
4. Security Group rules
5. Username
6. Password
7. Network accessibility

## Security

Do not store database passwords in this repository.

Use placeholders in documentation:

```text
<DB_USERNAME>
<DB_PASSWORD>
<DB_INSTANCE_ENDPOINT>
```

## Next Step

After establishing the connection, continue with:

```text
sql-operations.md
```

to practice SQL operations against the database.
