# 🏗️ ALB Architecture Overview

## Architecture Diagram

```text
                    Internet
                        │
                        ▼
          ┌────────────────────────────┐
          │  Application Load Balancer │
          └──────────────┬─────────────┘
                         │
                  Target Group
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼
      EC2 Instance 1         EC2 Instance 2
      Apache Web Server      Apache Web Server
```

---

## Request Flow

1. A client sends an HTTP request.
2. The Application Load Balancer receives the request.
3. The ALB forwards the request to the Target Group.
4. The Target Group distributes traffic across healthy EC2 instances.
5. If an instance becomes unhealthy, traffic is automatically redirected to healthy instances.

---

## Components

### 🌐 Application Load Balancer (ALB)

- Receives incoming HTTP requests
- Distributes traffic
- Performs health checks

### 🎯 Target Group

- Registers EC2 instances
- Routes traffic only to healthy targets

### 💻 EC2 Instances

- Host the web application
- Respond to client requests

### ❤️ Health Checks

The ALB continuously checks each EC2 instance.

If an instance fails the health check:

- It is marked **Unhealthy**
- Traffic is automatically redirected to healthy instances

---

## Benefits

- High Availability
- Fault Tolerance
- Better Scalability
- Improved Reliability

---

⭐ Architecture summary for AWS Application Load Balancer.