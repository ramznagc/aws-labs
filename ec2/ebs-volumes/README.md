# 💾 Amazon EC2 - EBS Volumes Management

> Hands-on lab demonstrating how to create, attach, extend, mount, and automatically mount Amazon EBS volumes on an EC2 instance.

---

# 📖 Overview

Amazon Elastic Block Store (EBS) provides persistent block storage for Amazon EC2 instances. In this lab, I learned how to resize the root volume, create and attach additional EBS volumes, mount them to Linux, extend their capacity, and configure automatic mounting after reboot.

--

# 🎯 Learning Objectives

After completing this lab, I was able to:

- Understand the difference between root and additional EBS volumes
- Extend the root volume of an EC2 instance
- Create and attach a new EBS volume
- Format and mount an EBS volume
- Resize an EBS volume without losing data
- Configure automatic mounting using `/etc/fstab`

---

# 🏗️ Architecture

```text
Amazon EC2
     │
     ├── Root Volume (EBS)
     │
     └── Additional EBS Volume
              │
              ▼
      Mounted to /mnt/2nd-vol
```

---

# Part 1 - Extend the Root Volume

Launch an EC2 instance with Amazon Linux 2023.

Verify the current storage:

```bash
lsblk
df -h
```

Check the filesystem:

```bash
sudo file -s /dev/nvme0n1p1
```

Increase the root volume size in the AWS Console.

Extend the partition:

```bash
sudo growpart /dev/nvme0n1 1
```

Resize the filesystem:

```bash
sudo xfs_growfs /dev/nvme0n1p1
```

Verify the result:

```bash
lsblk
df -h
```

---

# Part 2 - Create & Attach an Additional EBS Volume

Create a new 2 GB EBS volume in the same Availability Zone.

Attach it to the EC2 instance.

Verify:

```bash
lsblk
df -h
```

Check whether the disk is formatted:

```bash
sudo file -s /dev/nvme1n1
```

Format the volume:

```bash
sudo mkfs -t ext4 /dev/nvme1n1
```

---

# Part 3 - Mount the Volume

Create a mount point:

```bash
sudo mkdir /mnt/2nd-vol
```

Mount the volume:

```bash
sudo mount /dev/nvme1n1 /mnt/2nd-vol
```

Verify:

```bash
lsblk
df -h
```

Create a test file:

```bash
cd /mnt/2nd-vol
sudo touch hello.txt
```

---

# Part 4 - Extend the Additional Volume

Increase the volume size in AWS.

Resize the filesystem:

```bash
sudo resize2fs /dev/nvme1n1
```

Verify:

```bash
df -h
```

Ensure that `hello.txt` still exists.

---

# Part 5 - Configure Auto Mount

Backup the current fstab file:

```bash
sudo cp /etc/fstab /etc/fstab.bak
```

Edit fstab:

```bash
sudo nano /etc/fstab
```

Add:

```text
/dev/nvme1n1   /mnt/2nd-vol   ext4   defaults,nofail   0   0
```

Reboot the instance:

```bash
sudo reboot
```

Verify:

```bash
lsblk
df -h
```

---

# 💻 Linux Commands Used

```bash
lsblk
df -h
growpart
xfs_growfs
mkfs
mount
resize2fs
nano
```

---

# ✅ Validation Checklist

- Root volume successfully extended
- Additional EBS volume attached
- Filesystem formatted
- Volume mounted successfully
- Volume resized without data loss
- Auto-mount configured using fstab

---

# 💡 AWS Best Practices

- Always create snapshots before modifying EBS volumes.
- Keep backups of `/etc/fstab`.
- Use separate EBS volumes for application data.
- Monitor storage utilization regularly.
- Enable automatic mounting for persistent storage.

---

# 🧠 What I Learned

- EBS volume management
- Root volume expansion
- Filesystem resizing
- Linux mounting process
- Persistent storage configuration
- Auto-mount with `/etc/fstab`

---

# 🚀 Next Lab

➡️ EC2 Snapshots & Amazon Machine Images (AMI)