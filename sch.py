#!/usr/bin/python

from mylog import logger
import ConfigParser
import sys, re, os,time,commands


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
	except Exception,e:
		logger.error(str(e))
	finally:
	    return line

def func_schedule(cmds):
	try:
		print 'schedule executing...'
		#logger.info('scheduling...')
		#os.system(commands)
		#output = os.popen(cmds)
		#print output.read()
		(status, output) = commands.getstatusoutput(cmds)
		#print status,output
		if status != 0:
			logger.error('system cmds error:'+output)
	except Exception,e:
		logger.error('system cmds error:'+str(e))
		sys.exit(1)
	finally:
		return output
		
"""
def check_lock(lockfile):
	try:
		with open(lockfile,'r') as lk:
			pid = lk.read(10)
		os.kill(int(pid,0))
	except Exception,e:
		logger.error(str(e))
"""


if task_type == 'single':
	file_name = config.get('single_file_conf','in_file')
	if file_name is '' :
		print 'please config in_file name!'
		logger.error('conf error: in_file name is null')
		sys.exit(1)
	
	in_file = data_dir+'/'+file_name
	print 'in_file path:'+in_file
	logger.info('in_file path:'+in_file)
	if __name__ == '__main__':
		check_lock(FILE_PID)
		logger.info('running...')
		print func_read(in_file,separator)
		info_meta = func_read(path_file,separator)
		logger.info('program finished...')
		command = 'ls '+cm[0]+'| grep '+cm[1]
		func_schedule(command)	


if task_type == 'multi':
	if file_pattern is '' :
		print 'please config file_pattern!'
		logger.error('conf error: pattern error')
		sys.exit(1)
	all_files = [i for i in os.listdir(data_dir)]
	file_pattern = '^'+file_pattern+'$'
	
	files = [i.string for i in [re.match(file_pattern,j) for j in all_files ] if i]  
	files.sort()
	cnt = 0
	for fl in files:
		cnt += cnt
		path_file = os.path.join(data_dir,fl) 
		logger.info('path_file :'+str(cnt)+path_file)
		logger.info('running...')
		info_meta = func_read(path_file,separator)
		#print info_meta
		for cm in info_meta:
			command = 'ls '+cm[0]+'| grep '+cm[1]
			#print command
			inf = func_schedule(command)	
			logger.info(inf)	
		logger.info(str(fl)+' finished...')
time.sleep(0.5)
