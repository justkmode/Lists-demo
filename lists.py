# List of EC2 instance 
instance_ids = ["i-1234", "i-5678", "i-9012"]

# List of IP adresses for a security group
ip_addresses = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]

# List of availability zones in a region
availability_zones = ["eu-west-1a", "eu-west-2a", "eu-west-2c"]

# Print the lists
print(f"EC2 instances to terminate: {instance_ids}")
print(f"First IP addresses: {ip_addresses}")
print(f"Number of AZs: {availability_zones}")