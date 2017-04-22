# environment variables for rabbitmq server
export RABBITMQ_DEFAULT_USER=
export RABBITMQ_DEFAULT_PASS=
export RABBITMQ_DEFAULT_VHOST=
export BROKER_URL="amqp://$RABBITMQ_DEFAULT_USER:$RABBITMQ_DEFAULT_PASS@localhost:5672/$RABBITMQ_DEFAULT_VHOST"


# environment variables for postgres server
export POSTGRES_DATABASE=
export POSTGRES_USER=
export POSTGRES_PASSWORD=

# email configuration
export EMAIL_API_KEY=

# aws configuration
export AWS_ACCESS_KEY_ID=
export AWS_SECRET_ACCESS_KEY=
export AWS_DEFAULT_REGION=

#firebase configuration
export FIREBASE_CUSTOMER_KEY=

# server conf
export HOSTNAME=localhost
