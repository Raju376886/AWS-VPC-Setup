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


![image](https://github.com/user-attachments/assets/2faa57c7-2688-4f6e-8304-0307af3df7c1)

step-by-step process to implement this AWS infrastructure setup in your environment:

Step 1: Install and Configure AWS CLI
Before executing the script, ensure AWS CLI is installed and configured:
pip install awscli boto3
aws configure  # Enter your AWS Access Key, Secret Key, Region


Verify the AWS CLI is working:
aws ec2 describe-vpcs



Step 2: Set Up IAM Permissions
Ensure your AWS user has permissions to create:
- VPCs, Subnets, Route Tables
- Security Groups, EC2 Instances
- Elastic IP Allocation
- IAM Roles and Instance Profiles
Attach the required IAM policy if needed:
aws iam attach-user-policy --policy-arn arn:aws:iam::aws:policy/AmazonEC2FullAccess --user-name YOUR_USERNAME



Step 3: Execute Python Script
Run the Python script (modify AMI ID before running):
python AWS_CLI_Python.py


This will: ✔ Create a VPC
✔ Create a Subnet
✔ Attach an Internet Gateway
✔ Configure a Route Table
✔ Set Up a Security Group
✔ Create an IAM Role and Instance Profile
✔ Launch an EC2 instance
✔ Allocate and Associate an Elastic IP

Step 4: Verify Created Resources
Check each component manually:
- VPC:
aws ec2 describe-vpcs


- Subnet:
aws ec2 describe-subnets


- Security Group:
aws ec2 describe-security-groups


- EC2 Instance:
aws ec2 describe-instances



Step 5: Test Connectivity
- Ping Instance's Public IP:
ping <Elastic-IP>


- Try SSH Access:
ssh -i <YOUR_KEY.pem> ec2-user@<Elastic-IP>



Step 6: (Optional) Automate Key Pair Creation
Modify the script to generate a key pair:
key_pair = ec2.create_key_pair(KeyName='MyKeyPair')
with open("MyKeyPair.pem", "w") as key_file:
    key_file.write(key_pair['KeyMaterial'])


This will allow secure SSH login!

Step 7: Deploy Additional Security Enhancements
- Set up CloudWatch Monitoring
- Configure AWS Systems Manager for management
- Use Wazuh SIEM for log collection

Once implemented, your AWS environment will be fully automated! 

