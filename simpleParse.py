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

#��������
def parse(x):
	if 'attr' == x[0]:
    		#attr�����ز���
		attr.append(x)
	elif 'style' == x[0]:
		#style�����ز���
		style.append(x)
	elif 'layout' == x[0]:
		#layout�����ز���
		layout.append(x)
	elif 'drawable' == x[0]:
		#drawable�����ز���
		drawable.append(x)
	elif 'id' == x[0]:
		#id�����ز���
		_id.append(x)
	elif 'animator' == x[0]:
		#animator�����ز���
		animator.append(x)
	elif 'interpolator' == x[0]:
		#interpolator�����ز���
		interpolator.append(x)
	elif 'anim' == x[0]:
		anim.append(x)
	else:
		pass


#д���Ӧģ��

def write_modul(modul,out):
	for info in modul:
		#�����id�����ͽ��в���
		print info
		if '0x' in info[-1]:
		#�ҳ�name
			name = info[len(info)-2]
			_id = info[-1]
			out.write('        public static final int '+name+'='+_id+';'+'\n')

#����R�ļ�
def generate_R():
	out = open(sys.argv[2],'w')
	out.write('package com.bob;\n\npublic final class R {\n\n')
	#д�� anim
	out.write('    public static final class anim{\n')
	write_modul(animator,out)	
	write_modul(anim,out)	
	out.write('    }\n\n')

	#д�� attr
	out.write('    public static final class attr{\n')
	write_modul(attr,out)
	out.write('    }\n\n')
	
	#д�� drawable
	out.write('    public static final class drawable{\n')
	write_modul(drawable,out)
	out.write('    }\n\n')

	#д�� layout
	out.write('    public static final class layout{\n')
	write_modul(layout,out)
	out.write('    }\n\n')
	
	#д�� style
	out.write('    public static final class style{\n')
	write_modul(style,out)
	out.write('    }\n\n')

	#д�� id
	out.write('    public static final class id{\n')
	write_modul(_id,out)
	out.write('    }\n\n')

	#д������}
	out.write('\n}')
	out.close()

if __name__ == '__main__':	
	try:
		f = open(sys.argv[1],'r')
		for line in f.readlines():
			if('<public type' in line):
				#����ַ����������������			
				l = re.findall('"(.*?)"',line)
				#���ý�������
				parse(l)
		#��ɽ��������R.java�ļ����ɲ���
		generate_R()
	finally:
		if f:
			f.close()