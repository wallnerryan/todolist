
FROM ubuntu:14.04

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install git python python-pip python-setuptools python-MySQLdb

RUN git clone http://github.com/webpy/webpy /opt/webpy
WORKDIR /opt/webpy
RUN python setup.py install

ADD app/ /opt/app/
WORKDIR /opt/app/
EXPOSE 8080
CMD ["python","todo.py"]


