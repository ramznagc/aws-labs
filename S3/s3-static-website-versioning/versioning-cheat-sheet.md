# 📌 Amazon S3 Versioning Cheat Sheet

## What is Versioning?

Versioning protects objects from accidental deletion or overwriting by keeping multiple versions.

---

## Benefits

- Recover deleted files
- Restore previous versions
- Protect against accidental overwrite
- Improve data durability

---

## Versioning Workflow

Create Bucket

↓

Enable Versioning

↓

Upload Object

↓

Upload New Version

↓

Restore Previous Version

---

## Common Operations

- Enable Versioning
- List Versions
- Delete Marker
- Restore Previous Version

---

## Key Takeaways

- Every upload creates a new object version.
- Delete operations create a Delete Marker.
- Previous versions remain recoverable.