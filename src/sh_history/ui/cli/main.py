#!/usr/bin/env python
import click as C
from Clict import Clict
from sh_history.ui.cli.bash.main import bash_entry_point
from sh_history.ui.cli.setup import setup_entry_point

@C.group()
@C.pass_context
def cli_entry_point(ctx):
	"""	help cli"""
	# ensure that ctx.obj exists and is a dict (in case `cli()` is called
	# by means other than the `if` block below)
	ctx.ensure_object(Clict)
	ctx.obj.state=[]


@C.command(name='start')
@C.pass_context
def cmd_start(ctx):
	"""start new history session"""
	from sh_history.bash.main import start
	from sh_history.bash.vars import getvar
	ctx.obj=start(ctx.obj)
	vfile=getvar(ctx.obj, 'VARSFILE')
	C.echo(vfile)

@C.command(name='load')

@C.pass_context
def cmd_load(ctx):
	"""start new history session"""
	from sh_history.bash.main import start
	from sh_history.bash.vars import getvar

	vfile=getvar(ctx.obj, 'VARSFILE')
	C.echo(vfile)


cli_entry_point.add_command(bash_entry_point,name='bash')
cli_entry_point.add_command(setup_entry_point,name='setup')
cli_entry_point.add_command(cmd_start,name='start')
