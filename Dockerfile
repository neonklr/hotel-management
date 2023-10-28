# Setting base image
FROM python:3.11.6-slim-bullseye as python

# Update packages
RUN apt-get update

# Install git and curl
RUN apt-get install -y curl

# Install taskfile through official install.sh script
RUN sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d -b /usr/bin
