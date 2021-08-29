FROM ubuntu:20.04

WORKDIR /usr/src

COPY . .

RUN apt-get -y update && apt-get install -y python3
RUN apt-get -y install python3-pip 
RUN pip3 install --no-cache-dir -r requirements.txt
