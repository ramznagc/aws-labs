# 🚀 Amazon Linux 2023 AMI Cheat Sheet

## Get Latest AMI

```bash
aws ssm get-parameters \
--names /aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64
```

---

## Store AMI in Variable

```bash
ImageId=$(aws ssm get-parameters \
--names "/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64" \
--query 'Parameters[0].[Value]' \
--output text)
```

---

## Launch EC2

```bash
aws ec2 run-instances \
--image-id $ImageId \
--count 1 \
--instance-type t3.micro \
--key-name YOUR-KEY-NAME
```

---

## User Data

Launch an EC2 instance using a startup script to automate package installation and web server configuration.

---

## Best Practices

- Always retrieve the latest Amazon Linux AMI dynamically.
- Use variables to simplify automation scripts.
- Prefer User Data for repeatable EC2 provisioning.