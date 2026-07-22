# 🌐 Introduction to Computer Networks

> Hands-on notes and practical exercises covering the fundamentals of computer networking.

---

# 📖 Overview

Computer networking enables devices to communicate and share resources efficiently. Understanding networking fundamentals is essential for Cloud Computing, AWS, Linux administration, and DevOps.

This lab combines theoretical concepts with practical Linux networking commands to strengthen foundational networking skills.

---

# 🎯 Learning Objectives

After completing this lab, I was able to:

- Understand what a computer network is
- Explain the difference between LAN and WAN
- Identify common network components
- Understand transmission media
- Compare physical network topologies
- Use Linux commands to inspect network configuration

---

# 🌍 What is a Network?

A computer network is a group of interconnected devices that communicate and share resources.

Examples of shared resources include:

- File sharing
- Printers
- Email
- Databases
- Web applications
- VoIP
- Video conferencing

---

# 🏢 Local Area Network (LAN)

A Local Area Network (LAN) connects devices within a limited geographic area such as:

- Home
- School
- Office
- Campus

### Advantages

- High speed
- Low latency
- Easy resource sharing
- Cost effective

---

# 🌎 Wide Area Network (WAN)

A Wide Area Network (WAN) connects multiple LANs across large geographic areas.

Examples:

- Company branches
- Internet
- Cloud infrastructure

---

# 🖥️ Common Network Components

| Component | Description |
|-----------|-------------|
| Node | Any device connected to the network |
| Host | A device with an IP address |
| Client | Requests services |
| Server | Provides services |
| Switch | Connects devices in a LAN |
| Router | Connects different networks |

---

# 🔌 Transmission Media

### Guided Media

- Twisted Pair
- Coaxial Cable
- Fiber Optic

### Unguided Media

- Radio Waves
- Microwaves
- Infrared

---

# 🌐 Network Topologies

## Bus

✔ Simple

❌ Backbone failure affects entire network

---

## Star

✔ Easy to manage

✔ Most common topology

❌ Central switch is a single point of failure

---

## Ring

✔ Predictable communication

❌ Failure can interrupt the network

---

## Mesh

✔ High availability

✔ Fault tolerant

❌ Expensive

---

## Tree

✔ Scalable

✔ Organized hierarchy

❌ Root failure affects the network

---

## Hybrid

Combination of multiple network topologies.

---

# 💻 Mini Hands-on (Linux)

Display IP addresses

```bash
ip addr
```

Display routing table

```bash
ip route
```

Display hostname

```bash
hostname
```

Display local IP

```bash
hostname -I
```

Test connectivity

```bash
ping google.com
```

Display listening ports

```bash
ss -tuln
```

Display public IP

```bash
curl ifconfig.me
```

---

# 💡 Best Practices

- Use private IP addressing inside local networks.
- Segment large networks.
- Document network topology.
- Secure network devices.
- Monitor connectivity regularly.

---

# 🧠 What I Learned

- Network fundamentals
- LAN vs WAN
- Network devices
- Transmission media
- Physical topologies
- Basic Linux networking commands

---

# 🚀 Next Lab

➡️ TCP/IP & OSI Model
