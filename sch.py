#!/usr/bin/python

from mylog import logger
import ConfigParser
import sys, re, os

FILE_PID = 'sch.pid'

config = ConfigParser.RawConfigParser()
config.read('sch.conf')

task_type = config.get('task_type_conf','input_file_number')
data_dir = config.get('dir_conf','data_dir')
file_pattern = config.get('muti_file_conf','file_pattern')
separator = config.get('separator_conf','separator_character')


def func_read(filename,separator):
	line = []
	try:
		with open(filename,'r') as f:
			for lines in f:
				if lines.strip():
					line.append(tuple(lines.strip().split(separator)))
					
					#print line
	except Exception,e:
		logger.error(str(e))
	finally:
	    return line





if task_type == 'single':
	file_name = config.get('single_file_conf','in_file')
	if file_name is '' :
		print 'please config in_file name!'
		logger.error('conf error: in_file name is null')
		sys.exit(1)
	
	in_file = data_dir+'/'+file_name
	print 'in_file path:'+in_file
	logger.info('in_file path:'+in_file)
	print func_read(in_file,separator)

if task_type == 'multi':
	if file_pattern is '' :
		print 'please config file_pattern!'
		logger.error('conf error: pattern error')
		sys.exit(1)
	all_files = [i for i in os.listdir(data_dir)]
	file_pattern = '^'+file_pattern+'$'
	
	files = [i.string for i in [re.match(file_pattern,j) for j in all_files ] if i] #if i ?
	files.sort()
	cnt = 0
	for fl in files:
		cnt += cnt
		path_file = os.path.join(data_dir,fl) 
		logger.info('path_file :'+str(cnt)+path_file)
		print func_read(path_file,separator)
