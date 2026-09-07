# 🌐 Network 04 — IP Subnetting

## Overview

IP subnetting is the process of dividing a larger network into smaller logical networks.

It helps organize IP address space and create separate network segments.

## Network Structure

```text
Network
   │
   ├── Subnet 1
   │     ├── Hosts
   │     └── Hosts
   │
   ├── Subnet 2
   │     ├── Hosts
   │     └── Hosts
   │
   └── Subnet 3
         ├── Hosts
         └── Hosts
```

## CIDR and Subnetting

A CIDR prefix determines how many bits belong to the network portion of an IPv4 address.

```text
192.168.1.0/24
        │
        └── 24 network bits
```

A smaller prefix provides a larger address space, while a larger prefix creates smaller networks.

## Example

Starting network:

```text
192.168.1.0/24
```

Can be divided into smaller networks such as:

```text
192.168.1.0/26
192.168.1.64/26
192.168.1.128/26
192.168.1.192/26
```

## Why Subnet?

- Organize network resources
- Separate environments
- Improve address management
- Build scalable network architectures
- Create logical network boundaries

## Cloud Relevance

Subnetting is a fundamental concept for cloud networking and is directly related to designing public and private network segments in AWS VPC environments.

## Key Takeaway

```text
Large Network
      ↓
   Subnetting
      ↓
Smaller Networks
      ↓
Better Organization
```
