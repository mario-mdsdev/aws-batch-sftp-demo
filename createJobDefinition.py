import boto3

iam = boto3.client('iam')
client = boto3.client('batch')

role = iam.get_role(RoleName='dynamodbImportRole')

response = client.register_job_definition(
    jobDefinitionName='transfer_to_is_job_definition',
    type='container',
    containerProperties={
        'image': 'mdsdevhub/aws-batch-sftp-demo:latest',
        'jobRoleArn': role['Role']['Arn'],
        'executionRoleArn': role['Role']['Arn'],
        "logConfiguration": {
            "logDriver": "awslogs"
        },
        "resourceRequirements": [{
            "value": "0.25",
            "type": "VCPU"
        },{
            "value": "512",
            "type": "MEMORY"
        }],
        "networkConfiguration": {
            "assignPublicIp": "ENABLED"
        },
        'environment': [{
            'name': 'AWS_DEFAULT_REGION',
            'value': 'us-east-1'
        }],
        "fargatePlatformConfiguration": {
            "platformVersion": "LATEST"
        },
        "runtimePlatform": {
            "operatingSystemFamily": "LINUX",
            "cpuArchitecture": "X86_64"
        }
    },
    platformCapabilities=[
        "FARGATE"
    ]
)

print(response)