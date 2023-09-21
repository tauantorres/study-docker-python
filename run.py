from flask import Flask
import logging.config
import yaml

app = Flask(__name__)
with open('logging_config.yaml', 'rt') as f:
    config = yaml.safe_load(f.read())

logging.config.dictConfig(config)
logger = logging.getLogger('development')

@app.route('/', methods=["GET"])
def hello_world():
    logger.info("Starting app.")
    return "Testando a aplicação."
