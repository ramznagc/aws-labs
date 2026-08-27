# EFS Setup

## EC2 Security Group

Create a Security Group for the EC2 instances.

## EFS Security Group

Configure NFS access on TCP port 2049 from the EC2 Security Group.

## EC2 Instances

Launch two Amazon Linux 2023 EC2 instances.

## EFS Configuration

Create an encrypted Amazon EFS file system named `FirstEFS`.

## Network Configuration

Configure EFS mount targets and associate the EFS Security Group.