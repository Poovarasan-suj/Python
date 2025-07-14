import boto3
import time

# Create EC2 client
ec2 = boto3.client('ec2')

# Step 1: Get default VPC's subnet ID
vpcs = ec2.describe_vpcs(Filters=[{'Name': 'isDefault', 'Values': ['true']}])
vpc_id = vpcs['Vpcs'][0]['VpcId']

subnets = ec2.describe_subnets(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])
subnet_id = subnets['Subnets'][0]['SubnetId']

# Step 2: Launch EC2 instance with default subnet & security group
response = ec2.run_instances(
    ImageId='ami-020cba7c55df1f615',   # Amazon Linux 2 AMI
    InstanceType='t2.micro',
    KeyName='Mykey_ubuntu',                 # Replace with your key pair name
    MinCount=1,
    MaxCount=1,
    SubnetId=subnet_id,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'MyLearningInstance'}]
        }
    ]
)

# Get instance ID
instance_id = response['Instances'][0]['InstanceId']
print(f"EC2 instance launched: {instance_id}")

# Step 3: Wait until running
print("Waiting for instance to run...")
ec2.get_waiter('instance_running').wait(InstanceIds=[instance_id])

# Step 4: Get public IP
desc = ec2.describe_instances(InstanceIds=[instance_id])
public_ip = desc['Reservations'][0]['Instances'][0]['PublicIpAddress']
print(f"Public IP: {public_ip}")
