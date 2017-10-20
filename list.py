#removed debug statements. 
#Builds a list of filenames from an s3 bucket. 
#List is called oldlist.
import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('bucketname') # Replace bucketname with actual name of S3 bucket
oldlist=[]
for obj in bucket.objects.all():
    oldlist.append(obj.key)


