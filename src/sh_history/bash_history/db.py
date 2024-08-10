#!/usr/bin/env python
import click as C
from subprocess import getoutput
from sh_history.bash_history.env import getvar

def meta(ctx):
	id=ctx.obj.meta.id
	META_ID = int(getoutput(f'cat {getvar(ctx,"sysfull"")} |wc -l'))	+1
	META_TIME = "$TIMESTAMP"
	META_BOOT = "$(bash_bootstamp)"
	META_PID = "$$"
	META_DISTRO = '{NAME}-{VERS}'.format(NAME=getoutput('source /etc/lsb-release && echo {VAR}'.format(VAR='"$DISTRIB_ID"')),VERS=getoutput('source /etc/lsb-release && echo {VAR}'.format(VAR='"$VERSION_ID"')))
	META_HOST = "$HOSTNAME"
	META_USR = "$(whoami)"
	META_TTY = "$(tty)"
	META_BIN = "$SHELL"
	META_DIR = "$PWD"
	META_MD5 = "$( bash_history_md5 )"

	CSV = "${META_ID},${META_TIME},${META_MD5},${META_BOOT},${META_PID},${META_DISTRO},${META_HOST},${META_USR},${META_TTY},${META_BIN},${META_DIR},'${QCMD}'"



