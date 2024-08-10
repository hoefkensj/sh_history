#!/usr/bin/env python
import click
import click as C
from Clict import Clict,Clict_from
from pathlib import Path
from sh_history.bash_history import start,env

@C.command(name='start')
@C.pass_context
def entry_point(ctx):
	"""start help"""
	ctx=start.main(ctx)
	vfile=env.getvar(ctx, 'VARSFILE')
	C.echo(vfile)
