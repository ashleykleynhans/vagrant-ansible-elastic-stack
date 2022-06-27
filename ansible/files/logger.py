#!/usr/bin/env python3
import logging

APP_LOG_LEVEL = logging.DEBUG
ERROR_LOG_LEVEL = logging.ERROR
LOG_FORMATTER = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')


def setup_logger(name, log_file, level=logging.INFO):
    handler = logging.FileHandler(log_file)
    handler.setFormatter(LOG_FORMATTER)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


if __name__ == '__main__':
    app_logger = setup_logger('app', '/var/log/app.log', APP_LOG_LEVEL)
    error_logger = setup_logger('app-error', '/var/log/app-error.log', ERROR_LOG_LEVEL)

    app_logger.debug('This is debug')
    app_logger.info('This is info')
    app_logger.warning('This is warn')

    error_logger.error('This is an error')
    error_logger.critical('This is critical')
    error_logger.fatal('This is fatal')
