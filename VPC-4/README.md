# AWS LAMP Stack, WordPress & NACL

> Hands-on AWS project covering **LAMP Stack**, **WordPress**, **MariaDB**, **NAT Instance**, **Bastion Host**, and **Network ACLs**.

---

## 🏗️ Architecture

```text
                           AWS Cloud
                               │
                        ┌──────┴──────┐
                        │  ondia-vpc  │
                        │             │
              ┌─────────┴─────────────┴─────────┐
              │                                 │
              │          Public Subnet          │
              │                                 │
              │   ┌─────────────────────────┐   │
              │   │ WordPress / Bastion EC2 │   │
              │   │        Apache           │   │
              │   │          PHP            │   │
              │   │       WordPress         │   │
              │   └────────────┬────────────┘   │
              │                │                │
              │                │ MySQL :3306    │
              │                ▼                │
              │   ┌─────────────────────────┐   │
              │   │      Private EC2        │   │
              │   │        MariaDB          │   │
              │   │        ondiadb          │   │
              │   └─────────────────────────┘   │
              │                │                │
              │                │                 │
              │          Private Route Table     │
              │                │                 │
              │                ▼                 │
              │          NAT Instance            │
              │                │                 │
              └────────────────┼─────────────────┘
                               │
                               ▼
                           Internet