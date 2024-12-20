import logging
import logging.config

# Load logging configuration
logging.config.fileConfig('../logging.conf')

# Get the logger
logger = logging.getLogger('exampleLogger')

logger.info("This is a info message DDD")