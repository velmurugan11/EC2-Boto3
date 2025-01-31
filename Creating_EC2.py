import boto3

# Initialize EC2 resource
ec2 = boto3.resource("ec2", region_name="us-east-1")  # Change region if needed

# Create an EC2 instance
instance = ec2.create_instances(
    ImageId="ami-0c614dee691cbbf37",  # Amazon Linux 2 AMI (Change as per your region)
    MinCount=1,
    MaxCount=1,
    InstanceType="t2.micro",  # Free-tier eligible
    KeyName="KEY",  # Replace with your actual key pair name
    SecurityGroups=["default"],  # Replace with your security group name
    TagSpecifications=[
        {
            "ResourceType": "instance",
            "Tags": [{"Key": "Name", "Value": "MyBoto3Instance"}],
        }
    ],
)

print(f"Launching EC2 instance with ID: {instance[0].id}")