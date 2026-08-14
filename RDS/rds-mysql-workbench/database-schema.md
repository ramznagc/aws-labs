# Database Schema

## Overview

This document describes the logical structure of the sample MySQL database used in the project.

## Database

Example database:

```text
sampledb
```

## Tables

The database contains two related tables:

```text
sampledb
   │
   ├── offices
   │
   └── employees
```

## Offices Table

The `offices` table stores office information.

| Column      | Type        | Description    |
| ----------- | ----------- | -------------- |
| `office_id` | INT         | Primary key    |
| `address`   | VARCHAR(50) | Office address |
| `city`      | VARCHAR(50) | City           |
| `state`     | VARCHAR(50) | State          |

## Employees Table

The `employees` table stores employee information.

| Column        | Type        | Description       |
| ------------- | ----------- | ----------------- |
| `employee_id` | INT         | Primary key       |
| `first_name`  | VARCHAR(50) | First name        |
| `last_name`   | VARCHAR(50) | Last name         |
| `job_title`   | VARCHAR(50) | Job title         |
| `salary`      | INT         | Salary            |
| `reports_to`  | INT         | Manager reference |
| `office_id`   | INT         | Related office    |

## Relationship

The relationship between the tables is:

```text
offices
   │
   │ office_id
   │
   ▼
employees
```

The `employees.office_id` field references `offices.office_id`.

This relationship allows employee information to be combined with office information using an SQL `INNER JOIN`.

## Example Query

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

## Summary

The schema demonstrates a basic relational database model where employee records are associated with office records through a foreign key relationship.
