# Hands-on Lambda-01 — Lambda Function and API Gateway

This guide follows the supplied training material and organizes it into a cleaner step-by-step AWS lab.

## Learning Outcomes

By the end of the lab you will be able to:

- Create an S3 bucket.
- Create a Lambda function.
- Trigger Lambda with an S3 bucket event.
- Copy an object from one S3 bucket to another using Lambda.
- Create a Lambda function that generates a random city.
- Expose the Lambda function through API Gateway.

---

# Part 1 — Prepare S3

## Step 1 — Create the source bucket

Open **S3** in the AWS Console.

Create a bucket such as:

```text
ondia.source.lambda
```

Recommended lab configuration:

```text
Region                : US East (N. Virginia)
Block public access   : Enabled
Versioning            : Disabled
Tags                  : 0
Default encryption    : Default AWS setting
Object-level logging  : Disabled
```

S3 bucket names are globally unique. If the name is unavailable, use a unique suffix.

## Step 2 — Create the destination bucket

Create:

```text
ondia.destination.lambda
```

Use the same region and private-access baseline.

---

# Part 2 — S3 → Lambda → S3

## Step 1 — Create the IAM role

Open **IAM → Roles → Create role**.

Trusted entity:

```text
AWS service
```

Use case:

```text
Lambda
```

The original training material uses:

```text
Lambda.S3.Replica
```

and attaches:

```text
AmazonS3FullAccess
AWSLambdaBasicExecutionRole
```

For production, replace broad S3 access with a least-privilege policy.

## Step 2 — Create the Lambda function

Open:

```text
Lambda → Functions → Create function
```

Use:

```text
Name    : s3Duplicate
Runtime : Python 3.14
Role    : Lambda.S3.Replica
```

## Step 3 — Add the S3 trigger

In the Lambda designer, add an S3 trigger:

```text
Bucket     : ondia.source.lambda
Event type : All object create events
```

Keep public access blocked.

## Step 4 — Deploy the function

The cleaned-up implementation is:

```text
functions/s3_duplicate/lambda_function.py
```

The destination bucket can be configured through:

```text
DESTINATION_BUCKET
```

as a Lambda environment variable.

If it is not set, the training default is:

```text
ondia.destination.lambda
```

## Step 5 — Test object replication

Upload any file to the source bucket.

Then open the destination bucket.

Expected result:

```text
Source bucket
    │
    ├── example.txt
    │
    ▼
Lambda trigger
    │
    ▼
Destination bucket
    └── example.txt
```

---

# Optional Lambda Examples

## Example 1 — Random Roman Number

The original lab includes a function that generates a random number from 1 to 3999 and converts it to Roman numerals.

Source:

```text
functions/roman_number/lambda_function.py
```

Example:

```text
Roman Representation of the 2546 is MMDXLVI
```

## Example 2 — Event-based Roman Number

The original material also demonstrates receiving:

```json
{
  "num": 2546
}
```

and converting the value.

The repository keeps the concept in the Roman-number examples while presenting the implementation in a reusable form.

## Example 3 — Lambda Logging

The logging example uses Python's standard `logging` module and records:

- Lambda startup
- incoming event
- generated number
- conversion progress
- final Roman representation

The source is:

```text
functions/roman_number_with_logs/lambda_function.py
```

Logs can be inspected through Amazon CloudWatch Logs.

---

# Part 3 — Lambda + API Gateway

## Step 1 — Create the Lambda function

Open:

```text
Lambda → Functions → Create function
```

Use:

```text
Name    : RandomCityGenerator
Runtime : Python 3.14
```

The source is:

```text
functions/random_city/lambda_function.py
```

## Step 2 — Test the Lambda

Create a test event using an empty JSON object:

```json
{}
```

Run the test.

The function should return one city from the configured list.

---

# Step 3 — Create the API

Open:

```text
API Gateway → Create API
```

The original lab uses:

```text
Protocol     : REST
API name     : FirstAPI
Description  : test first api
Endpoint     : Regional
```

Create the API.

## Step 4 — Create `/city`

Create a resource:

```text
Resource path : /city
Resource name : city
```

Then create:

```text
GET /city
```

Integration:

```text
Integration type          : Lambda Function
Lambda Region              : us-east-1
Lambda Function            : RandomCityGenerator
Lambda Proxy Integration   : Off in the original lab
```

## Step 5 — Test the endpoint

Use the API Gateway **Test** operation.

The response should contain a random city.

Run the test multiple times to observe different results.

## Step 6 — Deploy the API

Create a stage:

```text
Stage name : dev
```

API Gateway will provide an account-specific invoke URL.

The final endpoint will have the form:

```text
https://<api-id>.execute-api.<region>.amazonaws.com/dev/city
```

Do not hard-code a real account-specific URL in source control.

Open the endpoint in a browser or HTTP client and refresh it to observe different city responses.

---

# Architecture Summary

## S3 Replication Demo

```text
┌───────────────────────┐
│ S3 Source Bucket     │
│ ondia.source.lambda  │
└──────────┬────────────┘
           │ ObjectCreated
           ▼
┌───────────────────────┐
│ Lambda                │
│ s3Duplicate           │
└──────────┬────────────┘
           │ copy_object()
           ▼
┌───────────────────────────┐
│ S3 Destination Bucket    │
│ ondia.destination.lambda │
└───────────────────────────┘
```

## API Demo

```text
┌───────────────┐
│ Browser /     │
│ HTTP Client   │
└───────┬───────┘
        │ GET /city
        ▼
┌───────────────────┐
│ API Gateway       │
│ FirstAPI /dev     │
└────────┬──────────┘
         ▼
┌────────────────────────┐
│ Lambda                 │
│ RandomCityGenerator    │
└───────────┬────────────┘
            ▼
       Random city
```

# Production Considerations

This is a teaching lab.

Before using the patterns in production:

- Use least-privilege IAM.
- Keep S3 Block Public Access enabled.
- Validate and decode S3 object keys when necessary.
- Consider duplicate-event/idempotency behavior.
- Configure CloudWatch log retention.
- Add API authentication/authorization where appropriate.
- Add error handling and retry/dead-letter strategies.
- Store resource names in configuration rather than hard-coding them.
