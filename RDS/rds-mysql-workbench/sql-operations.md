# MySQL SQL Operations

## Overview

This document contains example SQL operations used with the MySQL database.

The examples cover database creation, table creation, inserting data, retrieving records, filtering and joining related tables.

## Show Databases

```sql
SHOW DATABASES;
```

## Create a Database

```sql
CREATE DATABASE sampledb;
```

Select the database:

```sql
USE sampledb;
```

## Create the Offices Table

```sql
CREATE TABLE offices (
    office_id INT NOT NULL,
    address VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    PRIMARY KEY (office_id)
);
```

## Insert Data

```sql
INSERT INTO offices
    (office_id, address, city, state)
VALUES
    (1, '03 Reinke Trail', 'Cincinnati', 'OH');
```

Additional records can be inserted using the same structure.

## Create the Employees Table

```sql
CREATE TABLE employees (
    employee_id INT NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    job_title VARCHAR(50) NOT NULL,
    salary INT NOT NULL,
    reports_to INT DEFAULT NULL,
    office_id INT NOT NULL,
    PRIMARY KEY (employee_id),
    FOREIGN KEY (office_id)
        REFERENCES offices (office_id)
);
```

## Show Tables

```sql
SHOW TABLES;
```

## Query Data

Retrieve all offices:

```sql
SELECT * FROM offices;
```

Retrieve all employees:

```sql
SELECT * FROM employees;
```

## Filtering Data

Example:

```sql
SELECT *
FROM offices
WHERE state = 'OH';
```

## INNER JOIN

The `employees` and `offices` tables can be related through `office_id`.

```sql
SELECT
    employees.first_name,
    employees.last_name,
    employees.salary,
    offices.city,
    offices.state
FROM employees
INNER JOIN offices
    ON employees.office_id = offices.office_id;
```

## Filtering Joined Data

Example:

```sql
SELECT
    employees.first_name,
    employees.last_name,
    employees.salary,
    offices.city,
    offices.state
FROM employees
INNER JOIN offices
    ON employees.office_id = offices.office_id
WHERE employees.salary > 100000;
```

This query combines employee and office information and returns employees with salaries above `100000`.

## Common SQL Commands

```sql
SHOW DATABASES;

USE sampledb;

SHOW TABLES;

SELECT * FROM offices;

SELECT * FROM employees;
```

## SQL Workflow

```text
Connect
   │
   ▼
Select Database
   │
   ▼
Create Tables
   │
   ▼
Insert Data
   │
   ▼
Query Data
   │
   ▼
Filter / Join Data
```

## Learning Outcome

The exercises demonstrate basic relational database operations using MySQL.

Topics covered:

* Database creation
* Table creation
* Data insertion
* Data retrieval
* Filtering
* Primary keys
* Foreign keys
* INNER JOIN
* Relational data
