# NAT Gateway & NAT Instance

## NAT Gateway

A NAT Gateway provides internet connectivity for resources located in a private subnet.

```text
Private EC2
     │
     ▼
Private Route Table
     │
     ▼
NAT Gateway
     │
     ▼
Internet Gateway
     │
     ▼
Internet