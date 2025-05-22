# Test ELK Observability Stack with a Simple Web Application

This repository demonstrates how to use the Elastic Stack (Elasticsearch, Kibana, and APM Server) to observe a basic web application using OpenTelemetry automatic instrumentation.

It uses [EDOT](https://www.elastic.co/observability-labs/blog/elastic-distributions-opentelemetry) (Elastic Distribution of OpenTelemetry) to collect and export telemetry data to the Elastic Stack.

The web application is a simple FastAPI service that returns a JSON message when accessed at:

`curl http://localhost:8000/`

The ELK stack is provisioned via Docker Compose.

Logs, traces, and custom metrics (e.g., the endpoint_call_count metric) are captured and can be viewed in the Kibana UI.

## Getting Started

- Start the stack: `docker-compose up`
- Create the Kibana service token: `docker exec -it elasticsearch elasticsearch-service-tokens create elastic/kibana kibana-system`
- Copy the generated token and set it as the value of the `ELASTICSEARCH_SERVICEACCOUNTTOKEN` environment variable in the kibana service section of `docker-compose.yml`. 
- Restart Kibana: `docker compose up -d --force-recreate kibana`
- Access ElasticSearch at: http://localhost:5601 
  - Login with username: `elastic`, Password: `password`
- Install the APM integration with:
  - host = apm-server:8200
  - URL: http://apm-server:8200
- Hit the app to create some data: `curl http://localhost:8000/`
- Data should now be present in ElasticSearch