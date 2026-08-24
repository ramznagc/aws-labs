# AWS Lambda & API Gateway Hands-on Lab

![AWS Lambda Lab](assets/lambda-lab.jpg)

A hands-on AWS serverless lab covering **AWS Lambda, Amazon S3 event triggers, IAM roles, and Amazon API Gateway**.

The lab demonstrates two practical Lambda workflows:

1. **S3 → Lambda → S3** — automatically copy an object from a source bucket to a destination bucket.
2. **API Gateway → Lambda** — expose a Lambda function through a REST API that returns a random city.

> This repository is designed as a learning/demo project. AWS resource names and regions should be adjusted to match your own account.

## 🎯 Learning Outcomes

By completing this lab, you will learn how to:

- Create an Amazon S3 bucket.
- Create an AWS Lambda function.
- Create an IAM execution role for Lambda.
- Trigger Lambda from an S3 object-created event.
- Copy objects between S3 buckets with `boto3`.
- Create a Lambda function that generates a random city.
- Expose Lambda through Amazon API Gateway.
- Test a Lambda function directly and through an HTTP endpoint.
- Add structured logging for Lambda execution.

## 🧭 Lab Overview

```text
Part 1
S3 preparation
   │
   ├── Source bucket
   └── Destination bucket

Part 2
S3 Object Created
       │
       ▼
┌──────────────┐
│ AWS Lambda   │
│ s3Duplicate  │
└──────┬───────┘
       │
       ▼
Destination S3 bucket

Part 3
Browser / HTTP client
       │
       ▼
Amazon API Gateway
       │
       ▼
┌──────────────────────┐
│ AWS Lambda           │
│ RandomCityGenerator  │
└──────────┬───────────┘
           │
           ▼
       Random city
```

## 📁 Repository Structure

```text
.
├── assets/
│   └── lambda-lab.jpg
├── functions/
│   ├── s3_duplicate/
│   │   └── lambda_function.py
│   ├── random_city/
│   │   └── lambda_function.py
│   ├── roman_number/
│   │   └── lambda_function.py
│   └── roman_number_with_logs/
│       └── lambda_function.py
├── docs/
│   └── HANDS-ON-GUIDE.md
├── .gitignore
├── CHANGELOG.md
├── LICENSE
└── README.md
```

## 🧩 Part 1 — Prepare S3

Create two private S3 buckets in **US East (N. Virginia / us-east-1)**.

Suggested names:

```text
ondia.source.lambda
ondia.destination.lambda
```

Recommended baseline settings from the lab:

```text
Region                    : us-east-1
Block Public Access      : Enabled
Versioning               : Disabled
Tags                     : None
Object-level logging     : Disabled
```

For real AWS accounts, bucket names must be globally unique. Add a unique suffix if the suggested names are already taken.

## ⚡ Part 2 — S3 Event → Lambda

### IAM role

Create an IAM role for Lambda with:

```text
Trusted entity : AWS service
Use case       : Lambda
```

The original lab uses:

```text
Lambda.S3.Replica
```

For a learning environment it uses S3 access plus the basic Lambda execution policy.

For production, prefer a least-privilege policy scoped to the specific source and destination buckets rather than broad S3 permissions.

### Lambda function

Create:

```text
Function name : s3Duplicate
Runtime       : Python 3.14
```

Attach the Lambda execution role.

### S3 trigger

Configure an S3 trigger for the source bucket:

```text
Bucket     : ondia.source.lambda
Event type : All object create events
```

The Lambda function reads the uploaded object's bucket/key and copies the object to the destination bucket.

The implementation is available in:

```text
functions/s3_duplicate/lambda_function.py
```

### Test

Upload a file to the source bucket.

Then verify that the same object appears in the destination bucket.

```text
Source S3 bucket
      │
      │ ObjectCreated
      ▼
   Lambda
      │
      │ copy_object()
      ▼
Destination S3 bucket
```

## 🌍 Part 3 — Lambda + API Gateway

Create another Lambda function:

```text
Function name : RandomCityGenerator
Runtime       : Python 3.14
```

The function randomly selects one city from the sample list.

Example response:

```text
Istanbul
```

or:

```text
London
```

or:

```text
Paris
```

The source is:

```text
functions/random_city/lambda_function.py
```

### API Gateway

Create a REST API:

```text
API name     : FirstAPI
Endpoint     : Regional
Resource     : /city
Method       : GET
Integration  : Lambda
Function     : RandomCityGenerator
Stage        : dev
```

The resulting flow is:

```text
GET /city
    │
    ▼
API Gateway
    │
    ▼
RandomCityGenerator
    │
    ▼
Random city
```

The invoke URL will be account-specific, so do not hard-code an API Gateway URL in the repository.

## 🔢 Optional Lambda Examples

The lab also contains two small examples for converting numbers to Roman numerals.

### Roman number generator

```text
functions/roman_number/lambda_function.py
```

It generates a random number and returns its Roman representation.

### Roman number with logging

```text
functions/roman_number_with_logs/lambda_function.py
```

This version adds Python logging so execution details can be inspected through CloudWatch Logs.

## 🧪 Local Validation

The Python functions can be syntax-checked locally:

```bash
python -m py_compile functions/s3_duplicate/lambda_function.py
python -m py_compile functions/random_city/lambda_function.py
python -m py_compile functions/roman_number/lambda_function.py
python -m py_compile functions/roman_number_with_logs/lambda_function.py
```

The functions require AWS services when actually executed, so successful local syntax validation does not replace an AWS integration test.

## 🔐 Security Notes

This is a hands-on training repository, not a production reference architecture.

For production use:

- Avoid `AmazonS3FullAccess`.
- Restrict S3 permissions to the required buckets and actions.
- Keep S3 Block Public Access enabled.
- Avoid committing AWS credentials.
- Use environment variables or AWS-managed configuration for resource names.
- Keep API Gateway authorization/security requirements appropriate for the application.
- Review CloudWatch logging and retention settings.

## 📚 Full Hands-on Guide

The detailed step-by-step workflow is available here:

[`docs/HANDS-ON-GUIDE.md`](docs/HANDS-ON-GUIDE.md)

It covers:

- S3 bucket preparation
- IAM role
- Lambda creation
- S3 trigger
- S3 object replication
- Random city Lambda
- API Gateway REST API
- `/city` GET endpoint
- Lambda testing
- API deployment
- CloudWatch logging example

## 🗺️ Roadmap

- [ ] Add unit tests with `pytest`
- [ ] Add AWS SAM template
- [ ] Add least-privilege IAM policy examples
- [ ] Add automated deployment
- [ ] Add API Gateway authentication example
- [ ] Add CloudWatch log/metric configuration
- [ ] Add GitHub Actions CI

## 📄 License

MIT License. See [`LICENSE`](LICENSE).

## 👤 Author

**Ramazan Agac**

GitHub: https://github.com/ramznagc
