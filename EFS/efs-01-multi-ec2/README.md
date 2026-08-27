# AWS EFS - Multi-EC2 Linux File Sharing

## Overview

This project demonstrates how to create an Amazon Elastic File System (EFS) and attach the same shared file system to multiple Amazon EC2 Linux instances.

The project focuses on shared storage, Security Groups, NFS connectivity, Linux mount points and automatic mounting.

## Objectives

- Prepare EC2 and EFS Security Groups
- Launch multiple EC2 Linux instances
- Create an Amazon EFS file system
- Configure EFS mount targets
- Mount EFS on multiple EC2 instances
- Verify shared file access
- Configure automatic mounting with `/etc/fstab`
- Understand AWS shared storage concepts
- Clean up AWS resources after the lab

## Architecture

```text
                    AWS Cloud
                        │
                        ▼
                 ┌─────────────┐
                 │  Amazon EFS │
                 │   FirstEFS  │
                 └──────┬──────┘
                        │
              ┌─────────┴─────────┐
              │                   │
              ▼                   ▼
       ┌──────────────┐    ┌──────────────┐
       │ EC2 Instance │    │ EC2 Instance │
       │      1       │    │      2       │
       └──────────────┘    └──────────────┘
              │                   │
              └─────────┬─────────┘
                        │
                  Shared Files