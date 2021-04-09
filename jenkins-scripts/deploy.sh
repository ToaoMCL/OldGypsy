scp ./docker-compose.yaml jenkins@swarm-master:/home/jenkins/docker-compose.yaml
scp ./nginx/nginx.conf jenkins@swarm-master:/home/jenkins/nginx/nginx.conf
ssh jenkins@swarm-master << EOF
    docker stack deploy --compose-file /home/jenkins/docker-compose.yaml micro-service
EOF