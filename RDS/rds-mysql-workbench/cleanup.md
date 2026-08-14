# Cleanup

## Overview

AWS resources created for learning purposes should be reviewed after completing the lab.

Running resources may generate AWS charges.

## RDS Cleanup

After completing the project, review the RDS instance and determine whether it is still required.

If the database is no longer needed, remove it according to the lab requirements.

Before deleting the database, verify that no required data remains.

## Security Group

Review Security Groups created or modified for the project.

Remove unnecessary rules or resources when they are no longer required.

## Verification

After cleanup, verify that the resources used for the lab are no longer running unnecessarily.

Review:

```text
RDS
Security Groups
Networking resources
Other resources created during the lab
```

## Important

Do not delete resources that are used by other projects or environments.

Always verify the resource name and purpose before deleting it.

## Cost Awareness

Cloud resources can generate costs even when they are used only for learning.

A good cloud workflow includes:

```text
Create
   │
   ▼
Use
   │
   ▼
Verify
   │
   ▼
Clean Up
```

## Final Checklist

* [ ] Check RDS instance
* [ ] Remove unnecessary RDS resources
* [ ] Review Security Groups
* [ ] Review other resources created for the lab
* [ ] Verify that unnecessary resources are no longer running
