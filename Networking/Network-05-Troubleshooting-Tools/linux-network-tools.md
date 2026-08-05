# 🛠 Linux Network Troubleshooting Tools

## Connectivity

### ping

Checks whether a remote host is reachable.

```bash
ping google.com
```

---

## Routing

### traceroute

Displays every hop between source and destination.

```bash
traceroute google.com
```

---

## Live Path Analysis

### mtr

Combines ping and traceroute.

```bash
mtr google.com
```

---

## Network Configuration

### ip addr

Displays network interfaces.

```bash
ip addr
```

---

## ARP Cache

### ip neighbor

Shows IP-to-MAC address mappings.

```bash
ip neighbor
```

---

## DNS

### nslookup

Resolves domain names.

```bash
nslookup google.com
```

---

## Port Scan

### nmap

Scans TCP ports.

```bash
nmap -p 22,80,443 <ip-address>
```

---

## Routing Table

### ip route

Displays routing table.

```bash
ip route
```

---

## HTTP Test

### curl

Tests web services.

```bash
curl -I https://google.com
```

---

## Remote Access

### ssh

Secure remote login.

```bash
ssh ec2-user@server-ip
```

---

## Firewall

### iptables

Displays firewall rules.

```bash
sudo iptables -L
```