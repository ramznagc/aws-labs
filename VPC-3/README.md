# AWS VPC Peering & VPC Endpoint

> Hands-on AWS networking project covering **VPC Peering**, **NAT Gateway**, **Bastion Host**, and **S3 Gateway VPC Endpoint**.

---

## 🏗️ Project Architecture

```text
                         AWS Cloud
                             │
             ┌───────────────┴───────────────┐
             │                               │
       Default VPC                      aws-vpc-a
             │                               │
       Windows EC2                    ┌──────┴──────┐
       Public Subnet                  │             │
             │                   Public Subnet  Private Subnet
             │                         │             │
             │                    Bastion Host   Private EC2
             │                         │             │
             │                         │          ┌──┴──┐
             │                         │          │Nginx │
             │                         │          └─────┘
             │                         │
             └────── VPC Peering ─────┘