# 🔍 Network Troubleshooting Workflow

## Step 1

Verify connectivity.

```text
ping
```

↓

## Step 2

Analyze routing.

```text
traceroute
mtr
```

↓

## Step 3

Verify IP configuration.

```text
ip addr

ip route
```

↓

## Step 4

Verify DNS.

```text
nslookup

dig
```

↓

## Step 5

Test ports.

```text
nmap

telnet
```

↓

## Step 6

Test applications.

```text
curl
```

↓

## Step 7

Verify firewall.

```text
iptables
```

↓

## Step 8

Verify SSH connectivity.

```text
ssh
```

---

## Best Practices

- Start from Layer 3 connectivity.
- Verify DNS before troubleshooting applications.
- Test ports before checking services.
- Verify firewall configuration.
- Use systematic troubleshooting.