INSTANCE_NAME=rabbitmq-instance1
docker run -d \
    --hostname rabbitmq \
    -e RABBITMQ_DEFAULT_USER=$RABBITMQ_DEFAULT_USER -e RABBITMQ_DEFAULT_PASS=$RABBITMQ_DEFAULT_PASS \
    -p 4369:4369 -p5671:5671 -p 5672:5672 \
    --name $INSTANCE_NAME rabbitmq:3
