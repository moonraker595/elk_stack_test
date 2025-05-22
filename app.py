from fastapi import FastAPI
import logging
from opentelemetry import metrics

from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.metrics._internal.export import PeriodicExportingMetricReader

# Configure basic logging
logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level=logging.INFO)
logger = logging.getLogger("demoapp")

# Set up OTLP exporter
exporter = OTLPMetricExporter(
    endpoint="http://apm-server:8200/v1/metrics"
)

# Set up metric reader and provider
reader = PeriodicExportingMetricReader(exporter)
provider = MeterProvider(metric_readers=[reader])
metrics.set_meter_provider(provider)

# Set up a custom metric (Counter) to count calls to the endpoint
meter = metrics.get_meter("demoapp", "0.1.0")
request_counter = meter.create_counter("endpoint_call_count")

app = FastAPI()

@app.get("/")
def read_root():
    # Log a message for each request
    logger.info("Received request to root endpoint")
    # Record a metric data point for each request
    request_counter.add(1, {"endpoint": "/"})
    return {"message": "Hello, Observability!"}
