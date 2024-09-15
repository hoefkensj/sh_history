#!/usr/bin/env python
import click as C
from click_default_group import DefaultGroup
from Clict import Clict,Clict_from
from pathlib import Path
from sh_history.bash import env
import sys,os
from sh_history.tools import shell

@C.group(cls=DefaultGroup, default='show', default_if_no_args=True)
@C.pass_context
def grp_file(ctx):
	"""env help"""
	ctx.obj = env.init(ctx.obj)
	ctx.obj = env.load(ctx.obj)
	ctx.obj = env.scope(ctx.obj)
	return ctx

@C.command()
@C.argument('file', default=None)
@C.pass_context
def path(ctx,file):
	"""create help"""
	C.echo(env.getvar(ctx,file))

@C.command()
@C.pass_context
def list(ctx):
	"""create help"""

	for file in ctx.obj.scope:
		C.echo(file)

@C.command()
@C.argument('file', default=None)
@C.pass_context
def show(ctx,file):
	"""read help"""
	bat='env bat  --style full --force-colorization  --paging never --theme base16-256 '#Monokai\ Extended\ Origin '
	if file in ctx.obj.scope:
		if ctx.obj.scope[file].suffix == '.conf':
			bat+='--language conf '
		formatted=shell(f'{bat} {ctx.obj.scope[file]}\n')
	C.echo(formatted)



grp_file.add_command(path)
grp_file.add_command(list)
grp_file.add_command(show)


