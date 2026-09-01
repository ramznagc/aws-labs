# Bastion Host

## Purpose

A Bastion Host provides an SSH entry point for connecting to an EC2 instance located in a private subnet.

## Architecture

```text
Local Machine
     │
     │ SSH
     ▼
Public EC2
Bastion Host
     │
     │ SSH
     ▼
Private EC2