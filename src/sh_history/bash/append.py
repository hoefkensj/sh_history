#!/usr/bin/env python
from sh_history.bash import env
from sh_history.bash.main import load
from pathlib import Path
from subprocess import getoutput
import os



def cleanfile(file):
	getoutput(f"printf '' > {file}")


def main(ctx):
	from sh_history.tools import shell

	ctx=load(ctx)
	ctx.obj.timestamp=shell('date +%s')

	pid=ctx.obj.env.pid
	scope=ctx.obj.scope
	# ctx=lastcmd(ctx,scope)
	lastcmd=getoutput(f'cat {scope.lastcmd}')
	lastcmd+='\n'
	with open(scope.lastcmd, 'w') as l:
		l.write('')
	ctx.obj.cmd=lastcmd
	with open(scope.session, 'a') as s:
		 s.write(lastcmd)
	with open(scope.sysfull, 'a') as s:
		s.writelines(lastcmd)

	with open(scope.sysboot, 'a') as s:
		s.writelines(lastcmd)

	os.system(f"cat {scope.sysuniq} {scope.session} > {scope.histfile}")




	return ctx



