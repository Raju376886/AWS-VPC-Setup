# AWS-VPC-Setup
Python script that interacts with the AWS CLI via API calls to create a VPC, subnet, and a virtual machine (EC2 instance)

# AWS Infrastructure Automation

## Overview
This project automates the creation of an AWS Virtual Private Cloud (VPC), Subnet, Security Group, Route Table, Internet Gateway, and Elastic IP. Additionally, it launches an EC2 instance with proper IAM permissions and a security group.

## Features
- 🏗 **Creates VPC & Subnet** for a secure network architecture.
- 🔒 **Configures Security Group** to allow SSH (22) and HTTP (80).
- 🌐 **Sets Up Internet Gateway & Route Table** for external connectivity.
- 📌 **Allocates Elastic IP** for a static public IP.
- 🚀 **Deploys EC2 Instance** with IAM Role & Instance Profile.

## Prerequisites
Ensure you have the following installed:
- [AWS CLI](https://aws.amazon.com/cli/)
- [Boto3 (AWS SDK for Python)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- Python 3.x (`pip install boto3`)

## Installation
Clone the repository:
```sh
git clone https://github.com/Raju376886/AWS-VPC-Setup.git
cd AWS-VPC-Setup
