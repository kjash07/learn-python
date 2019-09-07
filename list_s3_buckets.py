import boto3

#s3_obj = boto3.resource('s3', aws_access_key_id="AKIAI4D2JRIXDDSXJXAQ", aws_secret_access_key="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")

s3_obj = boto3.resource('s3')

for each_object in s3_obj.buckets.all():
    print(each_object)
