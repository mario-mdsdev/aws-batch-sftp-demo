import boto3
import time

current_time = round(time.time() * 1000)

client = boto3.client('batch')

response = client.submit_job(
    jobDefinition='transfer_to_is_job_definition',
    jobName='transfer_to_is_job_' + str(current_time),
    jobQueue='transfer_to_is_job_queue',
    containerOverrides={
        'environment': [{
            'name': 'bucket_name',
            'value': 'batch-test-bucket-us-1'
        },{
            'name': 'key',
            'value': 'sample.csv'
        }]
    }
)

print(response)