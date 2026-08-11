# 🗄️ AWS RDS MySQL with MySQL Workbench

## Overview

This project documents the configuration of an Amazon RDS MySQL database and the process of connecting to it using MySQL Workbench.

The project covers:

- Amazon RDS configuration
- Security Group configuration
- MySQL Workbench connection
- Database and table creation
- SQL queries
- Data insertion
- JOIN operations
- RDS modification and deletion protection

---

## Architecture

```text
MySQL Workbench
       │
       │ MySQL : 3306
       ▼
┌───────────────────┐
│   AWS RDS MySQL   │
│                   │
│   clarusway DB    │
└───────────────────┘
       │
       ▼
   Security Group
```

---

## Topics Covered

### 1. RDS Configuration

- Create Security Group
- Configure MySQL/Aurora inbound access
- Create RDS MySQL instance
- Configure storage
- Configure connectivity
- Enable automatic backups
- Configure deletion protection

### 2. MySQL Workbench

- Configure a new connection
- Use the RDS endpoint
- Connect to the MySQL database
- Test the connection

### 3. SQL Operations

- Create databases
- Create tables
- Insert data
- SELECT queries
- WHERE filtering
- JOIN operations

---

## Project Structure

```text
rds-mysql-workbench
│
├── README.md
├── rds-configuration.md
├── mysql-workbench-connection.md
└── sql-operations.md
```

---

## Security Note

Never commit real database passwords, access keys, or other credentials to GitHub.

Use environment variables, AWS Secrets Manager, or another secure credential-management solution for sensitive information.

---

## Key Takeaway

Amazon RDS provides a managed relational database service while MySQL Workbench provides a convenient interface for connecting to and managing the database.