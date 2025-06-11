import boto3

# Initialize clients
ec2 = boto3.client('ec2')

# Step 1: Create VPC
vpc_response = ec2.create_vpc(CidrBlock='10.0.0.0/16')
vpc_id = vpc_response['Vpc']['VpcId']
print(f"Created VPC: {vpc_id}")

# Step 2: Create Subnet
subnet_response = ec2.create_subnet(VpcId=vpc_id, CidrBlock='10.0.1.0/24')
subnet_id = subnet_response['Subnet']['SubnetId']
print(f"Created Subnet: {subnet_id}")

# Step 3: Create Internet Gateway & Attach to VPC
igw_response = ec2.create_internet_gateway()
igw_id = igw_response['InternetGateway']['InternetGatewayId']
ec2.attach_internet_gateway(InternetGatewayId=igw_id, VpcId=vpc_id)
print(f"Created & Attached Internet Gateway: {igw_id}")

# Step 4: Create Route Table
route_table_response = ec2.create_route_table(VpcId=vpc_id)
route_table_id = route_table_response['RouteTable']['RouteTableId']
print(f"Created Route Table: {route_table_id}")

# Step 5: Associate Route Table with Subnet
ec2.associate_route_table(RouteTableId=route_table_id, SubnetId=subnet_id)

# Step 6: Add Internet Route to Route Table
ec2.create_route(
    RouteTableId=route_table_id,
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=igw_id
)
print("Added public internet access to Route Table")

# Step 7: Allocate & Associate Elastic IP to an Instance
eip_response = ec2.allocate_address(Domain='vpc')
eip = eip_response['PublicIp']
allocation_id = eip_response['AllocationId']
print(f"Allocated Elastic IP: {eip}")

# Step 8: Launch EC2 Instance
instance_response = ec2.run_instances(
    ImageId='ami-1234567890abcdef0',  # Replace with valid AMI
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1,
    SubnetId=subnet_id
)
instance_id = instance_response['Instances'][0]['InstanceId']
print(f"Launched EC2 Instance: {instance_id}")

# Step 9: Associate Elastic IP with EC2 Instance
ec2.associate_address(InstanceId=instance_id, AllocationId=allocation_id)
print(f"Associated Elastic IP {eip} with Instance {instance_id}")