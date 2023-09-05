import boto3

client = boto3.client('batch')

response = client.create_compute_environment(
    computeEnvironmentName='transfer_to_is_environment',
    type='MANAGED',
    state='ENABLED',
    computeResources={
        'type': 'FARGATE_SPOT',
        'allocationStrategy': 'BEST_FIT',
        'minvCpus': 0,
        'maxvCpus': 4,
        "subnets": [
            "subnet-0e8967cea32c6e3b0",
            "subnet-090b0aee595e37959",
            "subnet-0925f64f9b1534d0f",
            "subnet-0afa1e5af3fc049eb",
            "subnet-09dd9b9f7960baa03",
            "subnet-0cfa4c499dbf1973b"
        ],
        "securityGroupIds": [
            "sg-06b0ff0639bd599f3"
        ],
        'instanceTypes': [
            'optimal'
        ]
    }
)

print(response)