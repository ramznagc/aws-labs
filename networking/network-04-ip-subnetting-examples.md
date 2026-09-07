# IP Subnetting Examples

## /24 Network

```text
192.168.1.0/24
```

Subnet mask:

```text
255.255.255.0
```

## Four /26 Subnets

```text
192.168.1.0/26
192.168.1.64/26
192.168.1.128/26
192.168.1.192/26
```

Each subnet provides a separate network range.

## Visual View

```text
192.168.1.0/24
        │
        ├── 192.168.1.0/26
        ├── 192.168.1.64/26
        ├── 192.168.1.128/26
        └── 192.168.1.192/26
```

## Subnetting in Cloud

```text
                 VPC Network
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
       Public     Private     Private
       Subnet     Subnet      Subnet
```

Subnetting allows a larger network range to be organized into smaller logical segments.
