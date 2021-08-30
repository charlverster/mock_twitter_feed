# Use ubuntu 20.04 as base image
FROM ubuntu:20.04

# Set working directory
WORKDIR /usr/src

# Copy contents of local hosts working directory to working directory of container
COPY . .

# Install dependencies, specifcally python3 and pip3, then dependencies in requirements.txt
RUN apt-get -y update && apt-get install -y python3
RUN apt-get -y install python3-pip 
RUN pip3 install --no-cache-dir -r requirements.txt 
