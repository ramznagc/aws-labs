# ⚙️ AWS CLI Installation & Configuration

## Install AWS CLI

AWS CLI Version 2 can be installed on:

- Windows
- macOS
- Linux

---

## Verify Installation

```bash
aws --version
```

---

## Configure AWS CLI

Run the following command:

```bash
aws configure
```

You will be prompted to enter:

- AWS Access Key ID
- AWS Secret Access Key
- Default Region
- Default Output Format

Example:

```text
AWS Access Key ID [None]: ****************
AWS Secret Access Key [None]: ****************
Default region name [None]: us-east-1
Default output format [None]: yaml
```

---

## Useful Commands

List configured profiles:

```bash
aws configure list-profiles
```

Display current identity:

```bash
aws sts get-caller-identity
```

List S3 buckets:

```bash
aws s3 ls
```

---

## Multiple Profiles

Create a new profile:

```bash
aws configure --profile user1
```

Switch to another profile:

```bash
export AWS_PROFILE=user1
```

Return to the default profile:

```bash
export AWS_PROFILE=default
```

---

## Best Practices

- Protect your Access Keys.
- Follow the Principle of Least Privilege.
- Use multiple CLI profiles instead of replacing credentials.
- Verify your identity using `aws sts get-caller-identity`.