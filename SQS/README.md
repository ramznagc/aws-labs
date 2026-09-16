# 📬 Amazon SQS – Hands-on Lab

Practical AWS lab covering **Amazon SQS**, message handling, **AWS Lambda** integration, and **CloudWatch Logs**.

## 🎯 Learning Objectives

- Create an SQS queue
- Send, poll, receive, and delete messages
- Populate a queue with multiple messages
- Create a Lambda function from the SQS blueprint
- Connect Lambda to an SQS queue
- Enable the SQS trigger
- Verify processing through CloudWatch Logs
- Clean up created resources

## 🧩 Architecture

```text
Producer
   │
   ▼
SQS Queue
   │
   │ Message
   ▼
AWS Lambda
   │
   │ Execution Logs
   ▼
CloudWatch Logs
```

## 📌 Part 1 – Queue & Messages

### 1. Create Queue

Go to:

`SQS → Create queue`

| Setting | Value |
|---|---|
| Type | Standard |
| Name | `My-First-Queue` |

Keep Configuration, Access policy, Dead-letter queue, and remaining settings at their defaults.

### 2. Send Message

Open `My-First-Queue` → `Send and receive messages`.

Message:

```text
This is the first message for sqs.
```

After sending, verify:

`Messages available = 1`

### 3. Poll for Messages

Under `Receive messages`:

1. Select **Poll for messages**
2. Open the polled message
3. Verify its contents
4. Select **Done**
5. Delete the message

### 4. Populate Queue

Send three messages:

```text
This is the 2nd message for sqs.
This is the 3rd message for sqs.
This is the 4th message for sqs.
```

Poll and delete the messages after verification.

## ⚡ Part 2 – SQS → Lambda

### 1. Create Lambda Function

Go to:

`Lambda → Create function → Use a blueprint`

Search:

```text
sqs
```

Select:

```text
sqs-poller
```

Basic information:

| Setting | Value |
|---|---|
| Function name | `sqs-poller` |
| Execution role | Create a new role from AWS policy templates |
| Role name | `sqs-poller-role` |
| Policy template | Amazon SQS poller permissions |

SQS trigger:

```text
Queue: My-First-Queue
```

Create the function.

### 2. Enable Trigger

Open:

`Configuration → SQS: My-First-Queue`

Enable the trigger and wait until the status is:

`Enabled`

### 3. Send Message to Lambda

Return to SQS and send:

```text
This message is sent from sqs to trigger lambda
```

Verify that the message is polled and processed by Lambda.

### 4. Check CloudWatch Logs

Go to:

`CloudWatch → Logs → Log groups`

Open:

```text
/aws/lambda/sqs-poller
```

Open the relevant log stream and verify that the SQS message was processed by Lambda.

## 🧠 Key Takeaways

```text
Amazon SQS
├── Queue creation
├── Message sending
├── Message polling
├── Message receiving
└── Message deletion

AWS Lambda
├── SQS blueprint
├── SQS trigger
├── Trigger activation
└── Message processing

CloudWatch
└── Lambda execution logs
```

## 🧹 Cleanup

Delete/terminate the resources created during the lab.

---

⭐ **Hands-on AWS learning – Queues, Serverless & Event Processing**
