#!/bin/bash

docker run \
    -e POSTGRES_USER=template-test-admin \
    -e POSTGRES_PASSWORD=changeme \
    -e POSTGRES_DB=template_test \
    -e POSTGRES_SCHEMA=template_test \
    -p 5432:5432 \
    -v ~/docker_volumes/postgres-data/3.0-template-test:/var/lib/postgresql/data \
    -d -t -i --name 3.0-template-test-postgres 3.0-template-test-postgres
