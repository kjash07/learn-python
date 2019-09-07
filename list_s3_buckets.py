import boto3

s3_obj = boto3.resource('s3')

for each_object in s3_obj.buckets.all():
    #printing s3 buckets
    print(each_object)
