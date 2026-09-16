# 📢 Amazon SNS – Hands-on Lab

Practical AWS lab covering **Amazon SNS**, email subscriptions, message publishing, and **Amazon EventBridge → SNS** integration.

## 🎯 Learning Objectives

- Create an SNS topic
- Create and confirm an email subscription
- Publish a test message
- Create an EventBridge rule for EC2 state changes
- Send EventBridge events to an SNS topic
- Verify notifications by email
- Clean up created resources

## 🧩 Architecture

```text
EC2 Instance
     │
     │ State Change
     ▼
EventBridge Rule
     │
     ▼
SNS Topic
     │
     ▼
Email Subscription
```

## 📌 Part 1 – Topic, Subscription & Message

### 1. Create Topic

Go to:

`SNS → Topics → Create topic`

| Setting | Value |
|---|---|
| Type | Standard |
| Name | `Demo-topic` |
| Display Name | `My-First-Topic` |

Keep the remaining settings at their defaults and create the topic.

### 2. Create Subscription

Open `Demo-topic` → `Create subscription`.

| Setting | Value |
|---|---|
| Protocol | Email |
| Endpoint | Your email address |

The initial status should be:

`Pending Confirmation`

### 3. Confirm Subscription

Open the confirmation email from `My-First-Topic` and select **Confirm subscription**.

Refresh the SNS subscription page and verify:

`Status → Confirmed`

### 4. Publish Message

Open `Demo-topic` → `Publish message`.

| Setting | Value |
|---|---|
| Subject | `sns-test` |
| TTL | `-` |
| Message structure | Identical payload for all delivery protocols |

Message:

```text
This is a test message for sns inclass session
```

Publish the message and verify it in the subscribed email inbox.

## ⚡ Part 2 – EventBridge → SNS

### 1. Create Rule

Go to:

`Amazon EventBridge → Rules → Create Rule`

Configure:

| Setting | Value |
|---|---|
| Name | `EC2StateChange` |
| Event bus | `default` |
| Rule type | Rule with an event pattern |

Event pattern:

```text
Event source: AWS services
Service: EC2
Event type: EC2 Instance State-change Notification
State: Any state
Instance: Any instance
```

Target:

```text
Target type: AWS Service
Target: SNS topic
Topic: Demo-topic
```

Create the rule.

### 2. Trigger the Event

Open EC2 and change the state of an available instance, for example by starting a stopped instance.

### 3. Verify Notification

Check the subscribed email inbox and verify the notification generated through:

```text
EC2 → EventBridge → SNS → Email
```

## 🧠 Key Takeaways

```text
SNS
├── Topic
├── Subscription
├── Confirmation
└── Message publishing

EventBridge
├── EC2 event pattern
└── SNS target

Integration
└── EC2 → EventBridge → SNS → Email
```

## 🧹 Cleanup

Delete/terminate the resources created during the lab.

---

⭐ **Hands-on AWS learning – Messaging & Event-Driven Services**
