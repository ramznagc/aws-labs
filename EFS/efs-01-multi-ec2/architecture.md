# EFS Architecture

## Overview

This project demonstrates shared file storage using Amazon EFS with multiple EC2 Linux instances.

## Architecture

```text
AWS Cloud
    │
    ▼
Amazon EFS
  FirstEFS
    │
    ├───────────────┐
    ▼               ▼
 EC2-1            EC2-2
    │               │
    └───────┬───────┘
            ▼
      Shared Storage