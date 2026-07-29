# 🌐 IP Subnetting Fundamentals

## 📖 Overview

Subnetting is the process of dividing a large IP network into smaller, more manageable subnetworks. It improves network performance, reduces broadcast traffic, and simplifies administration.

---

## 🎯 Learning Objectives

After completing this topic, I can:

- Explain the purpose of subnetting
- Identify Network ID and Host ID
- Borrow host bits to create subnets
- Calculate subnet masks
- Determine valid host ranges
- Understand default gateways
- Explain CIDR notation

---

## 📌 Why Use Subnetting?

- Reduce network traffic
- Improve network performance
- Simplify network management
- Increase scalability
- Optimize IP address usage

---

## 🧩 Core Concepts

- Network ID
- Host ID
- Subnet ID
- Subnet Mask
- Broadcast Address
- Default Gateway
- CIDR Notation

---

## Example

Network:

192.168.123.0/24

Subnet Mask:

255.255.255.192

Subnets:

- 192.168.123.0/26
- 192.168.123.64/26
- 192.168.123.128/26
- 192.168.123.192/26

Hosts per subnet:

62

---

## Key Takeaways

- Subnetting creates smaller logical networks.
- Host bits are borrowed to create subnet bits.
- Every subnet has its own Network ID and Broadcast Address.
- CIDR notation simplifies subnet representation.

---

---

# 🧮 Subnetting Calculation Workflow

Follow these steps when solving subnetting problems:

1. Determine the required number of subnets.
2. Borrow the minimum number of host bits.
3. Calculate the new subnet mask.
4. Determine the block size.
5. Identify the Network Address.
6. Calculate the Broadcast Address.
7. Determine the first and last usable host addresses.

---

## Example

Network:

192.168.123.0/24

Required Subnets:

4

Borrowed Bits:

2

New CIDR:

/26

Subnet Mask:

255.255.255.192

Hosts per Subnet:

62

Block Size:

64