# 📌 Auto Scaling Policy Notes

## Simple Scaling

Uses one CloudWatch Alarm.

Example

CPU > 60%

→ Add 1 Instance

---

## Step Scaling

Scaling depends on CPU usage.

60% - 90%

→ Add 1 Instance

Above 90%

→ Add 2 Instances

---

## Target Tracking

AWS automatically keeps CPU utilization close to the target value.

Example

Target CPU

60%

---

## CloudWatch Metrics

- CPUUtilization
- NetworkIn
- NetworkOut
- Status Check
- Custom Metrics

---

## Best Practices

- Use Launch Templates
- Enable Health Checks
- Attach Target Groups
- Avoid aggressive scaling
- Monitor CloudWatch continuously

---

---

## 🧪 Hands-on Validation

After completing the lab, I verified that:

- EC2 instances were automatically registered to the Target Group.
- Health checks reported healthy targets.
- Auto Scaling replaced unhealthy instances.
- CloudWatch alarms triggered scaling actions.
- Application traffic was distributed through the ALB.