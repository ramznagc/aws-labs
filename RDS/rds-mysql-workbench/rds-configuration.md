# ⚙️ RDS MySQL Configuration

## 1. Create Security Group

Create a Security Group for the RDS database from the EC2 dashboard.

Example configuration:

```text
Security Group Name: clarusway_db_sg
Description: RDS MySQL Security Group
VPC: Default
```

### Inbound Rule

```text
Type: MYSQL/AURORA
Port: 3306
Source: My IP
```

Outbound rules can remain at their default configuration.

---

# 2. Create RDS Database

Open:

```text
AWS Console
→ RDS
→ Databases
→ Create database
```

Choose:

```text
Creation method:
Create with full configuration
```

---

# 3. Database Engine

```text
Engine: MySQL
```

Use the MySQL version required by the current lab environment.

---

# 4. Template

For learning environments:

```text
Template: Sandbox / Free Tier
```

Always verify current AWS pricing and Free Tier eligibility before creating resources.

---

# 5. Database Settings

Example:

```text
DB Instance Identifier: RDS-mysql
Master Username: admin
Master Password: YOUR_DB_PASSWORD
```

> Never commit the real master password to GitHub.

---

# 6. DB Instance Class

Example configuration from the lab:

```text
DB Instance Class:
Burstable classes

Instance:
db.t4g.micro
```

---

# 7. Storage

Example:

```text
Storage Type: SSD
Storage Size: 20 GiB
Storage Autoscaling: Enabled
Maximum Storage Threshold: 22 GiB
```

---

# 8. Connectivity

Example:

```text
VPC: Default
Subnet Group: Default
Publicly Accessible: Yes
Security Group: clarusway_db_sg
Port: 3306
```

The database should only be exposed to the required source IP when possible.

---

# 9. Authentication

```text
Database Authentication:
Password authentication
```

---

# 10. Additional Configuration

Example:

```text
Initial Database Name: clarusway

Parameter Group: default
Option Group: default

Automatic Backups: Enabled
Backup Retention: 7 days

Monitoring: Disabled
Log Exports: Disabled

Deletion Protection: Enabled
```

---

# 11. Important Concepts

## Automatic Backups

RDS automatic backups allow recovery of the database within the configured retention period.

## Maintenance

Minor version upgrades can be enabled for maintenance.

Major and minor version upgrades should be evaluated differently because major upgrades can introduce compatibility changes.

## Deletion Protection

Deletion protection prevents accidental deletion of the database instance.

This is especially useful for production databases.

---

# 12. Verify the Database

After creation, open the RDS database page and review:

- Connectivity & security
- Monitoring
- Configuration
- Maintenance
- Backups

The RDS endpoint will be required when configuring MySQL Workbench.