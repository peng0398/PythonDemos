# -*- coding: utf-8 -*-

import sys
import re

attr = []
style = []
layout = []
drawable = []
_id = []
animator = []
anim = []
interpolator =[]

#解析数据
def parse(x):
	if 'attr' == x[0]:
    		#attr类的相关操作
		attr.append(x)
	elif 'style' == x[0]:
		#style类的相关操作
		style.append(x)
	elif 'layout' == x[0]:
		#layout类的相关操作
		layout.append(x)
	elif 'drawable' == x[0]:
		#drawable类的相关操作
		drawable.append(x)
	elif 'id' == x[0]:
		#id类的相关操作
		_id.append(x)
	elif 'animator' == x[0]:
		#animator类的相关操作
		animator.append(x)
	elif 'interpolator' == x[0]:
		#interpolator类的相关操作
		interpolator.append(x)
	elif 'anim' == x[0]:
		anim.append(x)
	else:
		pass


#写入对应模块

def write_modul(modul,out):
	for info in modul:
		#针对有id的类型进行操作
		print info
		if '0x' in info[-1]:
		#找出name
			name = info[len(info)-2]
			_id = info[-1]
			out.write('        public static final int '+name+'='+_id+';'+'\n')

#生成R文件
def generate_R():
	out = open(sys.argv[2],'w')
	out.write('package com.bob;\n\npublic final class R {\n\n')
	#写入 anim
	out.write('    public static final class anim{\n')
	write_modul(animator,out)	
	write_modul(anim,out)	
	out.write('    }\n\n')

	#写入 attr
	out.write('    public static final class attr{\n')
	write_modul(attr,out)
	out.write('    }\n\n')
	
	#写入 drawable
	out.write('    public static final class drawable{\n')
	write_modul(drawable,out)
	out.write('    }\n\n')

	#写入 layout
	out.write('    public static final class layout{\n')
	write_modul(layout,out)
	out.write('    }\n\n')
	
	#写入 style
	out.write('    public static final class style{\n')
	write_modul(style,out)
	out.write('    }\n\n')

	#写入 id
	out.write('    public static final class id{\n')
	write_modul(_id,out)
	out.write('    }\n\n')

	#写入最终}
	out.write('\n}')
	out.close()

if __name__ == '__main__':	
	try:
		f = open(sys.argv[1],'r')
		for line in f.readlines():
			if('<public type' in line):
				#拆分字符串，方便后续解析			
				l = re.findall('"(.*?)"',line)
				#调用解析函数
				parse(l)
		#完成解析后进行R.java文件生成操作
		generate_R()
	finally:
		if f:
			f.close()