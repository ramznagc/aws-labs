# 💻 AWS CLI Command Reference

## IAM

```bash
aws iam list-users

aws iam create-user --user-name demo-user

aws iam delete-user --user-name demo-user
```

---

## Amazon S3

```bash
aws s3 ls

aws s3 mb s3://your-bucket

aws s3 cp file.txt s3://your-bucket

aws s3 rm s3://your-bucket/file.txt

aws s3 rb s3://your-bucket --force
```

---

## Amazon EC2

```bash
aws ec2 describe-instances

aws ec2 run-instances

aws ec2 stop-instances

aws ec2 terminate-instances
```

---

## Query Examples

```bash
--query

--filters

--output table

--output text
```

---

## Key Takeaways

AWS CLI commands follow a consistent structure:

aws <service> <operation> [options]