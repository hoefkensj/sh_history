#!/usr/bin/env python
import time
import hashlib
from subprocess import getoutput
import click as C
from sh_history.bash_history.

def md5hash(ctx,cmd):
	TIMESTAMP = getoutput('date +%s')

	MD5_HOST = ctx.obj.env.hosthame
	MD5_USER = ctx.obj.env.user
	MD5_TIME = TIMESTAMP
	MD5_CMD = cmd
	MD5_STR = f"{MD5_TIME}.{MD5_HOST}.{MD5_USER}.{MD5_CMD}"
	MD5_HASH = hashlib.md5(MD5_STR.encode()).hexdigest()

	return MD5_HASH



ctx=
md5hash(ctx,cmd)
