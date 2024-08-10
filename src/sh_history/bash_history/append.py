#!/usr/bin/env python
from sh_history.bash_history import env
from sh_history.bash_history.main import load
from pathlib import Path
from subprocess import getoutput
import os

def lastcmd(ctx,scope):
	with open(scope.histfile, 'r') as f:
		try:  # catch OSError in case of a one line file
			f.seek(-2, os.SEEK_END)
			while f.read(1) != b'\n':
				f.seek(-2, os.SEEK_CUR)
		except OSError:
			f.seek(0)
		last_line = f.readline()
	ctx.obj.cmd=last_line
	return ctx

def cleanfile(file):
	getoutput(f"printf '' > {file}")


def main(ctx):
	ctx=load(ctx)
	pid=ctx.obj.env.pid
	scope=ctx.obj.scope
	# ctx=lastcmd(ctx,scope)
	lastcmd=getoutput(f'cat {scope.lastcmd}')
	lastcmd+='\n'
	with open(scope.lastcmd, 'w') as l:
		l.write('')
	ctx.obj.cmd=lastcmd
	print(lastcmd)
	with open(scope.session, 'a') as s:
		 s.write(lastcmd)
	with open(scope.sysfull, 'a') as s:
		s.writelines(lastcmd)

	with open(scope.sysboot, 'a') as s:
		s.writelines(lastcmd)

	os.system(f"cat {scope.sysfull} {scope.sysboot} {scope.session} > {scope.histfile}")




	return ctx



