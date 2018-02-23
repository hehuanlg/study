import logging
'''
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)
logger.info('abc')
logger.debug('ccb')
'''

logger = logging.getLogger()
logger.setLevel(logging.INFO)

fh = logging.FileHandler('logfile.txt')
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)

fmt = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
fh.setFormatter(fmt)
ch.setFormatter(fmt)

logger.addHandler(fh)
logger.addHandler(ch)

logger.debug('abc')
logger.info('bbbc')
logger.warning('cdd')
logger.error('dee')
logger.critical('eaa')
