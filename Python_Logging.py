import logging
#logging.basicConfig(filename='../logs/k_mode.log')


logger = logging.getLogger()
logger.setLevel(logging.INFO)
#logger.setLevel(logging.WARN)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
#ch.setLevel(logging.WARN)


# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# Basic Information of the DataFrame
logger.info("This is a python log.\n")
