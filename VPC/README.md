# AWS VPC Configuration

## Overview

This project demonstrates the creation and configuration of an Amazon Virtual Private Cloud (VPC) with public and private subnets across multiple Availability Zones.

The main goal is to understand how a VPC, subnets, Internet Gateway and route tables work together to create a structured AWS networking environment.

## Project Goals

- Create a custom VPC
- Configure CIDR addressing
- Enable DNS hostnames
- Create an Internet Gateway
- Create public and private subnets
- Configure public and private route tables
- Associate subnets with route tables
- Enable automatic public IPv4 addresses for public subnets
- Launch EC2 instances in different subnets
- Compare private and public IP addresses
- Understand basic AWS network architecture

## Architecture

```text
                         AWS Cloud
                             │
                             ▼
                    ┌─────────────────┐
                    │   clarus-vpc-a  │
                    │   10.7.0.0/16   │
                    └────────┬────────┘
                             │
              ┌──────────────┴──────────────┐
              │                             │
              ▼                             ▼
       PUBLIC SUBNETS                PRIVATE SUBNETS
              │                             │
       ┌──────┼──────┐               ┌──────┼──────┐
       ▼      ▼      ▼               ▼      ▼      ▼
      AZ-1a  AZ-1b  AZ-1c           AZ-1a  AZ-1b  AZ-1c
       │      │      │               │      │      │
       └──────┼──────┘               └──────┼──────┘
              │                             │
              ▼                             ▼
      clarus-public-rt              clarus-private-rt
              │
              ▼
      clarus-igw
              │
              ▼
          Internet