#!/usr/bin/env python
import time
import hashlib
import os
from subprocess import getoutput
import click as C
from subprocess import getoutput
def md5hash(ctx,cmd):
	TIMESTAMP = getoutput('date +%s')

	MD5_HOST = ctx.obj.env.hosthame
	MD5_USER = ctx.obj.env.user
	MD5_TIME = TIMESTAMP
	MD5_CMD = cmd
	MD5_STR = f"{MD5_TIME}.{MD5_HOST}.{MD5_USER}.{MD5_CMD}"
	MD5_HASH = hashlib.md5(MD5_STR.encode()).hexdigest()

	return MD5_HASH



def shell(cmd,lines=1):
	result=getoutput(cmd)
	if lines == 1 :
		result=result.strip('\n')
	return result


def lastcmd(C,scope):
	with open(scope.histfile, 'r') as f:
		try:  # catch OSError in case of a one line file
			f.seek(-2, os.SEEK_END)
			while f.read(1) != b'\n':
				f.seek(-2, os.SEEK_CUR)
		except OSError:
			f.seek(0)
		last_line = f.readline()
	C.cmd=last_line
	return C
