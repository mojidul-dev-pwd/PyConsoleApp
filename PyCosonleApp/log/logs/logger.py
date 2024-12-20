import logging
"""
    filename='app.log',
    filemode='w',
    
    ##OR
    
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
    
"""


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)