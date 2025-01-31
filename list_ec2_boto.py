import boto3
from datetime import datetime,timedelta

def list_ec2_instances():
    # Create a session
    session = boto3.Session()
    
    # Get all available regions for EC2
    ec2_client = session.client('ec2')
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
    
    print(f"Found regions: {regions}")
    print("\nListing EC2 instances across all regions:\n")
    
    for region in regions:
        print(f"Region: {region}")
        ec2 = session.client('ec2', region_name=region)
        
        # Describe instances
        response = ec2.describe_instances()
        reservations = response.get('Reservations', [])
        
        if not reservations:
            print("  No instances found in this region.")
            continue

        
        for reservation in reservations:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                state = instance['State']['Name']
                instance_type = instance['InstanceType']
                launch_time = instance['LaunchTime']

                # Calculate how long the instance has been running.
                time_running = datetime.now(launch_time.tzinfo) - launch_time
                time_running_minutes = time_running.total_seconds() / 60  # in minutes
                
                print(f"  Instance ID: {instance_id}")
                print(f"  State: {state}")
                print(f"  Instance Type: {instance_type}")
                print(f"  Launch Time: {launch_time}")
                print(f"  Running Time: {time_running_minutes:.2f} minutes")
                

                # Check the instances is running more the a specific time.
                if time_running_minutes > 10 and state == 'running' or 'stopped':
                    print(f"  Terminating instance {instance_id}...")
                    ec2.terminate_instances(InstanceIds=[instance_id])
                    print(f"  Instance {instance_id} is terminated.")
                    # print(f"  Shutting down instance {instance_id}...")
                    # ec2.stop_instances(InstanceIds=[instance_id])
                    # print(f"  Instance {instance_id} is shutting down.")
                
                print("-" * 30)



if __name__ == "__main__":
    list_ec2_instances()
