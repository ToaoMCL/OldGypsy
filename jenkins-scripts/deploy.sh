scp -i ~/.ssh/id_rsa /home/jenkins/.jenkins/workspace/OldGypsy/docker-compose.yaml jenkins@swarm-master:home/jenkins/docker-compose.yaml
ssh jenkins@swarm-master << EOF
    docker stack deploy --compose-file home/jenkins/docker-compose.yaml micro-service
EOF