#!/usr/bin/env python
from sh_history.bash import env
from sh_history.tools import lastcmd

from pathlib import Path
from subprocess import getoutput
import os



def cleanfile(file):
	getoutput(f"printf '' > {file}")


def append(C):
	from sh_history.tools import shell

	C = env.init(C)
	C = env.read(C)
	C = env.load(C)
	C=lastcmd(C)
	C.vars.timestamp=shell('date +%s')

	pid=C.vars.pid
	scope=C.scope
	# C=lastcmd(C,scope)



	with open(scope.session, 'a') as s:
		 s.write(lastcmd)
	with open(scope.sysfull, 'a') as s:
		s.writelines(lastcmd)

	with open(scope.sysboot, 'a') as s:
		s.writelines(lastcmd)

	os.system(f"cat {scope.sysfull} {scope.sysboot} > {scope.histfile}")




	return C



