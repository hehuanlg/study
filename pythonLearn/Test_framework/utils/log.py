import logging
from logging.handlers import TimedRotatingFileHandler
from Test_framework.utils.config import LOG_PATH,Config

class Logger(object):
    def __init__(self,logger_name='framework'):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        self.log_file_name = 'test.log'
        self.backup_count = 5
        self.console_output_level = 'WARNING'
        self.file_output_level = 'DEBUG'
        self.formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

    def get_logger(self):
        if not self.logger.handlers:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)
            file_handler = TimedRotatingFileHandler(filename=LOG_PATH+self.log_file_name,
                                                    when='D',
                                                    interval=1,
                                                    backupCount=self.backup_count,
                                                    delay=True,
                                                    encoding='utf-8')
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger
logger = Logger().get_logger()
