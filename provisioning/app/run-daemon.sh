#!/bin/bash
docker run -d -t -i \
-e FLASK_APP="main" \
-e FLASK_APP=main \
-e FLASK_ENV=development \
-e FLASK_RUN_HOST=0.0.0.0 \
-e USER_NAME=kiosk-sandbox \
-e PASSWORD=NEM_vpu3xdy4jbh7vkd \
-e VAULT_URL=https://www.vault.setpoint.no:8200 \
-v /home/anup/resimator/Izy/izy-backend:/app \
-p 8081:80 \
  --restart no --name 3.0-template 3.0-template:1.0