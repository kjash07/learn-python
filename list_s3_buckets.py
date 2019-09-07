import boto3

s3_obj = boto3.resource('s3')

for each_object in s3_obj.buckets.all():
    print(each_object)
