#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import logging 
 
'''
log level:
    NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL
 
    logging.DEBUG
    logging.INFO
    logging.WARNING
    logging.ERROR
    logging.CRITICAL
 
'''
 
# 创建一个logger 
logger = logging.getLogger('mylogger') 
logger.setLevel(logging.DEBUG) 
   
# 创建一个handler，用于写入日志文件 
fh = logging.FileHandler('pro.log') 
fh.setLevel(logging.DEBUG) 
 
# 再创建一个handler，用于输出到控制台 
ch = logging.StreamHandler() 
ch.setLevel(logging.ERROR) 
   
# 定义handler的输出格式 
formatter = logging.Formatter('%(levelname)s [%(asctime)s] %(name)s:%(pathname)s [line %(lineno)d] [%(message)s]') 
fh.setFormatter(formatter) 
ch.setFormatter(formatter) 
   
# 给logger添加handler 
logger.addHandler(fh) 
logger.addHandler(ch)
 
if __name__ == '__main__':
 
    logger.debug('debug')   
    logger.info('info')
    logger.warning('warn')  
    logger.error('error') 
    try:
        print 1/0
    except Exception, e:
        logger.error(str(e[0]))
