#!/bin/bash

docker run \
    -e POSTGRES_USER=template-admin \
    -e POSTGRES_PASSWORD=changeme \
    -e POSTGRES_DB=template \
    -e POSTGRES_SCHEMA=template \
    -p 5432:5432 \
    -d -t -i --name 3.0-template-postgres 3.0-template-postgres
