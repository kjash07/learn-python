import boto3

ec2_obj = boto3.resource('ec2')

for obj in ec2_obj:
    