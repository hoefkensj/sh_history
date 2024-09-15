#!/usr/bin/env python
import os
from pathlib import Path

from Clict import Clict_from

from sh_history.tools import shell





def getvar(C, var):
	def descend(dct,var):
		result=None
		ret=None
		for item in dct:
			if isinstance(dct[item], dict):
				result = descend(dct[item], var)
			if item.casefold()==var.casefold() or item.casefold()==f'{C.env.shell}_{var}':
				result=dct[item]
				if isinstance(dct[item],dict):
					if 'val' in dct[item]:
						result=dct[item].val

			if result:
				ret=result
		return ret
	val=descend(C,var)
	return val


def setup(C):
	path=Path('/opt/local/sh_history/setup.conf')
	if path.exists():
		cfg=Clict_from.config(self={'path': path})
		for section in cfg:
			if len(cfg[section])!=0:
				for key in cfg[section]:
					C[section][key]=cfg[section][key]
	else :
		C.vars.hostname = shell('cat /proc/sys/kernel/hostname')
		C.vars.domain = None
		C.vars.os = os_version()
		C.vars.install_folder ='/opt/local/sh_history/'
		C.vars.log_folder ='/var/cache/history/'
	return C


def os_version():
	ov = '{NAME}-{VERS}'.format(
	NAME=shell('source /etc/lsb-release && echo {VAR}'.format(VAR='"$DISTRIB_ID"')),
	VERS=shell('source /etc/os-release && echo {VAR}'.format(VAR='"$VERSION_ID"')))
	return ov


def dynamic(C):
	#dynamic:
	C.vars.bootstamp=shell("uptime -s | tr -d '\-: '")
	C.vars.pid=os.getppid()
	C.vars.shell = 'bash'
	C.vars.user=shell('whoami')
	C.vars.tty=shell('readlink /proc/self/fd/0')
	C.vars.pwd=shell('pwd')
	return C

def vars(C):
	C=setup(C)
	C=dynamic(C)
	return C
