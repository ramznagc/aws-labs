# 🌍 Amazon S3 Bucket Replication Guide

## Replication Requirements

- Source bucket
- Destination bucket
- Versioning enabled
- IAM Role
- Replication Rule

---

## Replication Types

### Entire Bucket Replication

Replicates all objects from the source bucket.

### Prefix Replication

Replicates only objects within a specific folder.

### Tag Replication

Replicates only objects with specific object tags.

---

## Benefits

- Disaster Recovery
- High Availability
- Multi-Region Architecture
- Compliance

---

## Key Takeaways

Replication requires versioning and an IAM role with the required S3 permissions.