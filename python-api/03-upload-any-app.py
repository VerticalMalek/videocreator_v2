import boto3

s3 = boto3.resource('s3')
MY_BUCKET = '200543'
bucket = s3.Bucket(MY_BUCKET)

with open ('serce.txt', 'rb') as to_be_uploaded:

        bucket.put_object(
        Key = "foo/moo/boo/zoo/serce.txt",
        Body= to_be_uploaded
        )