#!/usr/bin/env python
import time
import hashlib
import os
from subprocess import getoutput
import click as C
from subprocess import getoutput
def md5hash(C):
	MD5_VERS = 1.0e1
	MD5_TIME = C.vars.time
	MD5_DOMAIN = C.vars.domain
	MD5_HOST = C.vars.host
	MD5_USER = C.vars.user
	if C.command is not None:
		MD5_CMD = C.command
	else:
		MD5_CMD = C.cmd
	MD5_STR = '.'.join([i for i in [MD5_DOMAIN,MD5_HOST,MD5_USER,MD5_TIME,MD5_CMD] if i != ''])
	MD5_HASH = hashlib.md5(MD5_STR.encode()).hexdigest()
	C.meta.hash=MD5_HASH
	print(C.meta.hash)
	return C



def shell(cmd,lines=1):
	result=getoutput(cmd)
	if lines == 1 :
		result=result.strip('\n')
	return result


def lastcmd(C):
	print(repr(C))
	with open(C.env.read.FILES.BASH_LASTCMD, 'r') as f:
		try:  # catch OSError in case of a one line file
			f.seek(-2, os.SEEK_END)
			while f.read(1) != b'\n':
				f.seek(-2, os.SEEK_CUR)
		except OSError:
			f.seek(0)
		last_line = f.readline()
	C.cmd=last_line
	with open(C.lastcmd, 'w') as l:
		l.write('')
	return C
