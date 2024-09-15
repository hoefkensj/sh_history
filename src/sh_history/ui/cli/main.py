#!/usr/bin/env python
import click as C
from Clict import Clict
from sh_history.ui.cli.bash.main import bash_entry_point
from sh_history.ui.cli.setup import setup_entry_point
from sh_history.bash.append import append
from sh_history.bash.main import start
from sh_history.bash.vars import getvar
from sh_history.bash import env
@C.group()
@C.pass_context
def cli_entry_point(ctx):
	"""	help cli"""
	# ensure that C.obj exists and is a dict (in case `cli()` is called
	# by means other than the `if` block below)
	ctx.ensure_object(Clict)
	ctx.obj.state=[]


@C.command()
@C.pass_context
def cmd_start(ctx):
	"""start new.0 history session"""
	O=ctx.obj
	O = env.init(O)
	O = env.create(O)
	O = env.write(O)
	O = env.load(O)
	O = env.read(O)

	vfile=getvar(ctx.obj, 'VARSFILE')
	C.echo(vfile)

@C.command()
@C.argument('key', default=None)
@C.pass_context
def cmd_get(ctx,key):
	"""get value for ke"""
	ctx.obj = env.init(ctx.obj)
	ctx.obj = env.load(ctx.obj)
	ctx.obj = env.read(ctx.obj)
	vfile=getvar(ctx.obj, key)
	C.echo(vfile)

@C.command()
@C.pass_context
def cmd_append(ctx):
	"""append help"""
	ctx.obj=append(ctx.obj)

cli_entry_point.add_command(bash_entry_point,name='bash')
cli_entry_point.add_command(setup_entry_point,name='setup')
cli_entry_point.add_command(cmd_start,name='start')
cli_entry_point.add_command(cmd_get,name='get')
cli_entry_point.add_command(cmd_append,name='append')
