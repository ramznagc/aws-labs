# AWS VPC — Bastion Host & NAT

## Overview

This project demonstrates how to securely access private EC2 instances and provide outbound internet connectivity from a private subnet using AWS networking components.

The project covers:

- Bastion Host
- SSH Agent Forwarding
- Private EC2 access
- NAT Gateway
- Elastic IP
- Private Route Table
- NAT Instance
- Source/Destination Check

## Architecture

```text
                         Internet
                            │
                            ▼
                     ┌──────────────┐
                     │ Public Subnet│
                     │              │
                     │ Bastion Host │
                     └──────┬───────┘
                            │
                         SSH -A
                            │
                            ▼
                    ┌───────────────┐
                    │ Private Subnet│
                    │               │
                    │  Private EC2  │
                    └───────────────┘