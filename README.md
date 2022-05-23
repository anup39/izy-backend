# izy-restx-3.0-template

### Prerequisites

1. Python 3.9
2. PostgreSQL 12.3 - https://hub.docker.com/layers/postgres/library/postgres/12.3/images/sha256-a8250a7c7f7f95da67e691e9af8e7ca772c1aacdd1c71634a4bb48c6d0eee071?context=explore

## Creating and running postgres docker container

To set up local DB container you need:
1. Navigate to `./provisioning/postgres` directory
2. Run build script `./build.sh` to build postgres docker image
3. Run `docker network create postgresql` to create new network
4. Run daemon script `./run-deamon.sh` to run docker container

```
export FLASK_APP=main
export USER_NAME=kiosk-sandbox
export PASSWORD='NEM_vpu3xdy4jbh7vkd'
export VAULT_URL=https://www.vault.setpoint.no:8200
```

As a result after running command `docker ps -a` you should see created postgres container with status `Up` in the listing.

## Building and running the project in docker

For running project in a Docker container you need:

Check if docker is installed:
```bash
docker -v
```

As a result command prompt should print message like this:
```
Docker version 18.09.3, build 774a1f4
```

Move to `provisioning/app/` folder and run:
```bash
./build.sh
```
and then
```bash
./run-daemon.sh
```

As a result after running the command `docker ps -a` you should see created container with status `Up` in the listing.

To migrate the database, run the following script located inside the container:
```
/provisioning/migrate.sh
```


If this endpoint fails, the migration has most likely failed.


# Openapi integration

To use swagger ui as openapi implementation follow the link `http://localhost:8081/api`



