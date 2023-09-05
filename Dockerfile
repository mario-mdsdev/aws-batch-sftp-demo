FROM amazonlinux:latest
RUN yum -y install which unzip python3-pip
RUN pip3 install boto3
ADD sendToSFTP.py /usr/local/bin/sendToSFTP.py
WORKDIR /tmp
USER nobody
ENTRYPOINT ["/usr/local/bin/sendToSFTP.py"]
