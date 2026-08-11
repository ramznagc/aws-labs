# 🔌 MySQL Workbench Connection

## 1. Get RDS Endpoint

Open:

```text
AWS Console
→ RDS
→ Databases
→ RDS-mysql
```

Find the database endpoint under the connectivity section.

The endpoint will be used as the MySQL Workbench host.

---

## 2. Open MySQL Workbench

Open MySQL Workbench and select:

```text
MySQL Connections
→ +
```

Create a new connection.

---

## 3. Connection Configuration

Example:

```text
Connection Name:
RDS MySQL

Hostname:
YOUR_RDS_ENDPOINT

Port:
3306

Username:
admin
```

---

## 4. Password

Select:

```text
Store in Keychain / Vault
```

Enter the database password securely.

Do not write the password inside the project files.

---

## 5. Test Connection

Click:

```text
Test Connection
```

If the configuration is correct, MySQL Workbench should successfully connect to the RDS instance.

---

## 6. Connection Flow

```text
MySQL Workbench
       │
       │
       │ Port 3306
       ▼
Security Group
       │
       ▼
AWS RDS MySQL
       │
       ▼
clarusway Database
```

---

## Troubleshooting Checklist

If the connection fails, check:

- RDS instance status
- RDS endpoint
- Port 3306
- Security Group inbound rule
- Source IP
- Username
- Password
- Public accessibility
- Network connectivity