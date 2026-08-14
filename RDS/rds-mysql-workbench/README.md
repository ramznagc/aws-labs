# Amazon RDS MySQL with MySQL Workbench

## Overview

This project documents the configuration and use of an Amazon RDS for MySQL database and the process of connecting to it using MySQL Workbench.

The project focuses on understanding managed relational databases on AWS, network connectivity, database access and basic SQL operations.

## Objectives

- Understand Amazon RDS for MySQL
- Configure an RDS database instance
- Configure database connectivity
- Understand Security Group rules
- Connect to RDS using MySQL Workbench
- Create and manage databases and tables
- Execute SQL queries
- Practice relational database operations
- Document the complete workflow

## Architecture

```text
                    AWS Cloud
                       │
                       │
                ┌──────▼──────┐
                │  Amazon RDS │
                │    MySQL    │
                └──────┬──────┘
                       │
                  TCP 3306
                       │
                ┌──────▼──────┐
                │    MySQL    │
                │  Workbench  │
                └─────────────┘