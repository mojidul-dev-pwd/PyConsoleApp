
from logger import logging

logging.debug("This is a debug message")
logging.info("This is a info message")
logging.warning("This is a warning message")
logging.error("This is a error message")
logging.critical("This is a critical message")

def add(x,y):
    result = x+y
    message = "Addition method executed. Result = "+str(result)
    logging.info(message)
    return result

add(5,6)