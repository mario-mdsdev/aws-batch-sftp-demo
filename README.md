# AWS Batch SFTP Demo

This demo application aims to test AWS Batch to transfer a file from S3 bucket to an external SFTP using Python library paramiko.  

### Change in sendToSFTP.py file the 'sftp_hostname' and 'sftp_username' values

### Replace the pkey file content with your private key value

### Replace in docker commands below the docker hub account to yours

```bash
docker build -f Dockerfile -t mdsdevhub/aws-batch-sftp-demo \
 --build-arg AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
 --build-arg AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
 --build-arg AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION .
```

```bash
docker push mdsdevhub/aws-batch-sftp-demo
```

### Change the file createComputeEnvironment.py with your subnets and security group ids

```bash
python createComputeEnvironment.py
```

```bash
python createJobQueue.py
```

### Change the file createJobDefinition.py with your RoleName and docker hub image

```bash
python createJobDefinition.py
```

### Submit a new Job (do not forget to change the job name before each run)

```bash
python createJob.py
```
