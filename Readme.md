# Kpax Scripts

Scripts to help the fast configuration of virtual machines and servers.
A make file to unite and rule any EC2 instance.


- [Kpax Scripts](#kpax-scripts)
  - [Scripts](#scripts)
    - [Install python 3.9](#install-python-39)
    - [Install Docker and docker compose](#install-docker-and-docker-compose)
    - [Install AWS CLI](#install-aws-cli)
    - [System checks](#system-checks)
  - [Make Commands](#make-commands)
    - [Check](#check)
    - [Complete setup](#complete-setup)


## Scripts

The main folder that holds the shell scripts

### Install python 3.9
    Gives you a python installation for the 3.9 version 

### Install Docker and docker compose
    Install Docker from the repo

### Install AWS CLI
    Install AWS CLI and other dependecies

### System checks
    Executes a simple system check


## Make Commands

A collection of ultra useful make commands
The main goal is to provide a fast boiler plate setup to EC2 instances.

### Check 

Executes a routine check

### Complete setup

Executes the following commands:

- [***Install python 3.9***](./scripts/setup_python3_9.sh)
- [***Install Docker***](./scripts/install_docker.sh)
- [***Install AWS CLI***](./scripts/install_aws.sh)