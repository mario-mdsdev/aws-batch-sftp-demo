FROM amazonlinux:latest

RUN yum -y install which unzip python3-pip
RUN yum clean all

WORKDIR /app

ADD sendToSFTP.py pkey /app/

ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_DEFAULT_REGION

RUN pip3 install boto3 paramiko

USER nobody

CMD ["python3", "/app/sendToSFTP.py"]
