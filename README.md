# EC2-Boto3
# AWS Boto3 EC2 Projects

This repository contains two separate Python scripts that interact with AWS EC2 using the Boto3 library:

1. **List EC2 Instances** - Lists all EC2 instances in a given AWS account.
2. **Create EC2 Instance** - Creates a new EC2 instance using predefined configurations.

## Prerequisites

- Python 3.x
- Boto3 library
- AWS credentials configured via the AWS CLI or environment variables.

### Install Boto3

```bash
pip install boto3
```

## 1. List EC2 Instances

### Description
This script fetches and lists all EC2 instances in a specified AWS region. It shows details like instance ID, state, type, and public IP.

### Usage

```bash
python list_ec2_instances.py
```

### Script Details
- **AWS Region**: By default, it will use `us-east-1`, but you can modify it within the script or set it via environment variables.
- **IAM Role Permissions**: Ensure your AWS IAM role or user has the `ec2:DescribeInstances` permission.

### Example Output
```bash
Instance ID: i-1234567890abcdef0
Instance State: running
Instance Type: t2.micro
Public IP: 198.51.100.1

Instance ID: i-0abcdef1234567890
Instance State: stopped
Instance Type: t2.medium
Public IP: None
```

## 2. Create EC2 Instance

### Description
This script launches a new EC2 instance based on a predefined configuration. You can modify parameters like instance type, AMI, key pair, etc.

### Usage

```bash
python create_ec2_instance.py
```

### Script Details
- **AMI ID**: Set the correct AMI ID for the region.
- **Instance Type**: Default set to `t2.micro`. Change this in the script if you need a different type.
- **Key Pair**: You must specify an existing key pair to SSH into the instance after creation.
- **Security Group**: The script uses an existing security group (default group `default`).

### Example Output
```bash
Launching EC2 Instance...
Instance created successfully.
Instance ID: i-0987654321abcdef0
Public IP: 54.123.45.67
```

## Configuration

1. **AWS Credentials**: Make sure your AWS credentials are configured. You can configure them using AWS CLI by running:

   ```bash
   aws configure
   ```

   Or, alternatively, you can export the following environment variables:

   ```bash
   export AWS_ACCESS_KEY_ID="your-access-key-id"
   export AWS_SECRET_ACCESS_KEY="your-secret-access-key"
   export AWS_DEFAULT_REGION="your-region"
   ```

2. **Region Configuration**: In both scripts, the AWS region can be modified. Make sure you're working in the correct region for your EC2 instances.

## Notes

- Ensure your AWS IAM permissions allow for EC2 operations (`ec2:DescribeInstances`, `ec2:RunInstances`, etc.).
- Always be careful with creating EC2 instances as it may incur charges depending on your instance type and usage.
- For a successful EC2 creation, verify that the AMI ID, instance type, key pair, and security groups are correctly configured.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or issues with this project, feel free to reach out at [your-mvel3987@gmail.com].
```

Let me know if you'd like to adjust anything further!
