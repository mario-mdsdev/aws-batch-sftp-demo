import boto3

client = boto3.client('batch')

response = client.create_job_queue(
    jobQueueName='transfer_to_is_job_queue',
    state='ENABLED',
    priority=1,
    computeEnvironmentOrder=[
        {
            'order': 100,
            'computeEnvironment': 'transfer_to_is_environment'
        }
    ]
)

print(response)