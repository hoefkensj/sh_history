#!/usr/bin/env python
import click
import click as C
from Clict import Clict,Clict_from,to_config
from pathlib import Path

from  sh_history.bash.vars import vars
from sh_history.bash import env

@C.command(name='setup')
@C.pass_context
def setup_entry_point(ctx):
	"""start help"""
	ctx.obj = env.init(ctx.obj)
	ctx.obj = env.read(ctx.obj)
	C=ctx.obj
	C=setup(C)





def setup(c):
	C.echo('Setup: ')
	C.echo('\x1b[35G\x1b[4mDetected\x1b[m\n\x1b[15G\x1b[36m{key}\x1b[35G\x1b[1;32m{val}\x1b[m'.format(key='Hostname:', val=c.vars.get('host')))
	C.echo('\x1b[15G\x1b[36m{key}\x1b[35G\x1b[1;32m{val}\x1b[m'.format(key='Domain:', val=c.vars.get('domain')))
	C.echo('\x1b[15G\x1b[36m{key}\x1b[35G\x1b[1;32m{val}\x1b[m'.format(key='Os/distro:', val=c.vars.get('os')))
	C.echo('\x1b[15G\x1b[36m{key}\x1b[35G\x1b[1;32m{val}\x1b[m'.format(key='Log Folder:', val=c.vars.get('folder_log')))
	C.echo('\x1b[15G\x1b[36m{key}\x1b[35G\x1b[1;32m{val}\x1b[m'.format(key='Install Folder:', val=c.vars.get('folder_conf')))
	# C.obj.env.shell=C.prompt('Shell:',default=C.obj.env.get('shell'))
	# C.obj.env.shell=C.prompt('User:',default=C.obj.env.get('user'))
	s=Clict()
	s.vars.host=C.prompt('Host', default=c.vars.get('host'))
	s.vars.domain=C.prompt('Domain', default=c.vars.get('domain'))
	s.vars.os=C.prompt('Os/Distro', default=c.vars.get('os'))
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
