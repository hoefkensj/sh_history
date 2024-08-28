#!/usr/bin/env python
import click
import click as C
from Clict import Clict,Clict_from,to_config
from pathlib import Path

import sh_history.bash.vars
from sh_history.bash import env

@C.command(name='setup')
@C.pass_context
def setup_entry_point(ctx):
	"""start help"""
	ctx.obj = env.init(ctx.obj)
	ctx.obj = env.read(ctx.obj)
	ctx.obj = env.scope(ctx.obj)
	C=ctx.obj
	C=setup(C)





def setup(c):
	C.echo('Setup: ')
	C.echo('\x1b[5GDetected: \x1b[15G\x1b[36m{key}\x1b[30G\x1b[1;32m{val}\x1b[m'.format(key='Hostname:', val=sh_history.bash.vars.vars.get('hostname')))
	C.echo('\x1b[15G\x1b[36m{key}\x1b[30G\x1b[1;32m{val}\x1b[m'.format(key='Domain:', val=sh_history.bash.vars.vars.get('domain')))
	C.echo('\x1b[15G\x1b[36m{key}\x1b[30G\x1b[1;32m{val}\x1b[m'.format(key='Os/distro:', val=sh_history.bash.vars.vars.get('os')))
	C.echo('\x1b[15G\x1b[36m{key}\x1b[30G\x1b[1;32m{val}\x1b[m'.format(key='Log Folder:', val=sh_history.bash.vars.vars.get('folder_log')))
	C.echo('\x1b[15G'
	'\x1b[36m{key}\x1b[30G\x1b[1;32m{val}\x1b[m'.format(key='Install Folder:', val=sh_history.bash.vars.vars.get('folder_conf')))
	# ctx.obj.env.shell=C.prompt('Shell:',default=ctx.obj.env.get('shell'))
	# ctx.obj.env.shell=C.prompt('User:',default=ctx.obj.env.get('user'))
	s=Clict()
	s.vars.host=C.prompt('Host', default=sh_history.bash.vars.vars.get('hostname'))
	s.vars.domain=C.prompt('Domain', default=sh_history.bash.vars.vars.get('domain'))
	s.vars.os=C.prompt('Os/Distro', default=sh_history.bash.vars.vars.get('os'))
	s.vars.folder_log=C.prompt('History Log Folder',default='/var/cache/history/')
	s.vars.folder_conf=Path(C.prompt('History Install Folder',default='/opt/local/sh_history/'))

	setup=Path(s.vars.folder_conf,'setup.conf')
	installdir=s.vars.folder_conf
	installdir.mkdir(mode=0o777,parents=True,exist_ok=True)
	to_config(s,setup)


#     "domain"                 TEXT,
#     "host"                   TEXT,
#     "user"                   TEXT,
#     "tty"                    TEXT,
#     "shell"                  TEXT,
#     "pwd"                    TEXT,
#     "exitcode"               TEXT,
#     "command"                TEXT,
#     PRIMARY KEY("index" AUTOINCREMENT)
# )
