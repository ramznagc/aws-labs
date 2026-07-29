# 📌 IP Subnetting Cheat Sheet

## IPv4 Structure

Network ID + Host ID

---

## Subnetting Formula

Borrow Host Bits

↓

Create Subnets

↓

Reduce Hosts

---

## Common CIDR Values

| CIDR | Subnet Mask | Hosts |
|------|-------------|------:|
| /24 | 255.255.255.0 | 254 |
| /25 | 255.255.255.128 | 126 |
| /26 | 255.255.255.192 | 62 |
| /27 | 255.255.255.224 | 30 |
| /28 | 255.255.255.240 | 14 |
| /29 | 255.255.255.248 | 6 |

---

## Reserved Addresses

First Address

→ Network Address

Last Address

→ Broadcast Address

---

## Default Gateway

Used to communicate with devices outside the local subnet.

---

## CIDR Examples

192.168.1.10/24

172.16.10.5/28

10.0.0.15/16