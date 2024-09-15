#!/usr/bin/env python
import os,sys,re,platform
from pathlib import Path
from Clict import Clict,Clict_from
from sh_history.bash import env

def load(C):
	C = env.init(C)
	C = env.read(C)
	C = env.load(C)
	C = env.scope(C)
	return C

def start(C):
	C=env.start(C)
	C=env.scope(C)
	# os.system(f"cat {scope.sysfull} {scope.sysboot} |tac|awk '!seen[$$0]++'|tac > {scope.sysuniq}")
	return C

def show(C):
	C=load(C)
	return C

#
# h.id
