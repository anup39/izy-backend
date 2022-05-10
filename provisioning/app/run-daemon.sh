#!/bin/bash
docker run -d -t -i -e FLASK_APP="main" \
-e FLASK_APP=main \
-e FLASK_CONFIG=production \
-e USER_NAME=user-management \
-e PASSWORD=ehn2cqa6FEN9mcf.kfq \
-p 8081:80 \
  --restart no --name 3.0-template 3.0-template:1.0