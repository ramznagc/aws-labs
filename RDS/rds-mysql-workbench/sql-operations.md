# 🧮 SQL Operations with RDS MySQL

## 1. Create Table

Example:

```sql
CREATE TABLE `clarusway`.`Personal_Info_2` (
    `ID_number` INT NOT NULL,
    `Name` VARCHAR(45) NULL,
    `Surname` VARCHAR(45) NULL,
    `Gender` VARCHAR(45) NULL,
    `Age` INT NULL,
    `Department` VARCHAR(45) NULL,
    PRIMARY KEY (`ID_number`)
);
```

---

# 2. Insert Data

```sql
INSERT INTO clarusway.Personal_Info_2
(ID_number, Name, Surname, Age, Department)
VALUES
('1234','Osvaldo','Clarusway','43','dev'),
('56789','Guile','Clarusway','34','dev'),
('007','Charlie','Clarusway','54','devops'),
('432','Marcus','Clarusway','32','test'),
('324','Vincenzo','Clarusway','25','dev'),
('4587','Aslan','Clarusway','61','test'),
('43546','Serdar','Clarusway','37','devops');
```

---

# 3. Select All Data

```sql
SELECT *
FROM clarusway.Personal_Info_1;
```

---

# 4. Filter Data

Find people whose salary is greater than 40,000:

```sql
SELECT *
FROM clarusway.Personal_Info_1
WHERE salary > 40000;
```

---

# 5. JOIN Tables

Join `Personal_Info_1` and `Personal_Info_2` using `ID_number`:

```sql
SELECT
    p1.Name,
    p1.Surname,
    p2.Department,
    p1.Salary
FROM clarusway.Personal_Info_1 AS p1
JOIN clarusway.Personal_Info_2 AS p2
ON p1.ID_number = p2.ID_number;
```

---

# 6. JOIN with Filtering

Find people whose salary is greater than 50,000 and display their department:

```sql
SELECT
    p1.Name,
    p1.Surname,
    p2.Department,
    p1.Salary
FROM clarusway.Personal_Info_1 AS p1
JOIN clarusway.Personal_Info_2 AS p2
ON p1.ID_number = p2.ID_number
WHERE p1.Salary > 50000;
```

---

# 7. SQL Workflow

```text
Create Database
      ↓
Create Table
      ↓
Insert Data
      ↓
SELECT
      ↓
WHERE
      ↓
JOIN
      ↓
Analyze Results
```

---

# Key Takeaways

- RDS provides the managed MySQL database.
- MySQL Workbench provides the database management interface.
- SQL is used to create, modify, retrieve and combine data.
- JOIN operations allow related data from multiple tables to be queried together.