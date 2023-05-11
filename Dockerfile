FROM centos:7

RUN yum -y update
RUN yum -y install epel-release && yum clean all
RUN yum -y install python3 python3-pip

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./usermanager /app
WORKDIR /app

RUN python3 manage.py collectstatic --noinput
RUN chmod -R 755 /app
RUN python3 manage.py makemigrations && python3 manage.py migrate

