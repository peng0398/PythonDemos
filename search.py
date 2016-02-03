#-*- coding:utf-8 –*-
import os
import os.path
rootdir="/home/bob/桌面/Develop/facebook/fresco-master"

def count_flag(filepath,flag):
	try:
		f = open(filepath, 'r')
		for line in f.readlines():
			if(flag in line):
				print(line)
	finally:
		if f:
			f.close()



for parent,dirnames,filenames in os.walk(rootdir): 
	for filename in filenames:                      
		if(os.path.join(parent,filename).endswith('.java')):
			count_flag(os.path.join(parent,filename),'SimpleDraweeView')


