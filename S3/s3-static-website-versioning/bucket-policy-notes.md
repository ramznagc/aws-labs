# 🔐 Amazon S3 Bucket Policy Notes

## What is a Bucket Policy?

A bucket policy is a JSON-based access policy that defines who can access an S3 bucket and what actions they are allowed to perform.

---

## Common Permissions

- s3:GetObject
- s3:PutObject
- s3:DeleteObject
- s3:ListBucket

---

## Public Read Policy Example

```json
{
  "Version":"2012-10-17",
  "Statement":[
    {
      "Effect":"Allow",
      "Principal":"*",
      "Action":"s3:GetObject",
      "Resource":"arn:aws:s3:::YOUR_BUCKET_NAME/*"
    }
  ]
}
```

---

## Best Practices

- Enable Block Public Access unless required.
- Grant the minimum required permissions.
- Avoid using wildcard permissions unless necessary.
- Review bucket policies regularly.

---

## Key Takeaways

- Bucket policies control access at the bucket level.
- Public website hosting requires read access.
- Always follow the Principle of Least Privilege.