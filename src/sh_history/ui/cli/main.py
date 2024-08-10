#!/usr/bin/env python
import click as C
from Clict import Clict

@C.group()
@C.pass_context
def entry_point(ctx):
	"""	help cli"""
	# ensure that ctx.obj exists and is a dict (in case `cli()` is called
	# by means other than the `if` block below)
	ctx.ensure_object(Clict)
	ctx.obj.state=[]

@C.command()
@C.pass_context
def bash(ctx):
	"""bash help"""
	pass
from sh_history.ui.cli.bash import main

entry_point.add_command(main.entry_point,name='bash')
