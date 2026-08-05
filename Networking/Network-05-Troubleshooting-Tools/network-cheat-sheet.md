# 📋 Linux Network Cheat Sheet

| Tool | Purpose |
|-------|---------|
| ping | Verify connectivity |
| traceroute | Display routing path |
| mtr | Continuous path monitoring |
| ip addr | Show interfaces |
| ip neighbor | Show ARP cache |
| nslookup | DNS lookup |
| nmap | Scan ports |
| ip route | Routing table |
| telnet | Test TCP connectivity |
| curl | Test web servers |
| ssh | Secure remote access |
| iptables | Host firewall |

---

## Quick Commands

```bash
ping google.com

traceroute google.com

mtr google.com

ip addr

ip neighbor

nslookup google.com

nmap -p 22,80 google.com

ip route

curl -I https://google.com

ssh ec2-user@server

sudo iptables -L
```

---

## Troubleshooting Order

1. Ping

2. Traceroute

3. IP Configuration

4. DNS

5. Ports

6. HTTP

7. Firewall

8. SSH