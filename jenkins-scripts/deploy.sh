scp ./docker-compose.yaml jenkins@swarm-master:/home/jenkins/docker-compose.yaml
ssh jenkins@swarm-master << EOF
    export DB_URI=${DB_URI}
    export app_version=${app_version}
    docker stack deploy --compose-file /home/jenkins/docker-compose.yaml micro-service
EOF