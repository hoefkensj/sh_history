#!/usr/bin/env python
import click as C
from Clict import Clict,Clict_from
from pathlib import Path
from sh_history.bash import env
import sys,os
from sh_history.tools import shell

@C.group()
@C.pass_context
def grp_env(ctx):
	"""env help"""
	pass


@C.command()
@C.pass_context
def create(ctx):
	"""create env vars from sys config"""
	ctx.obj=env.create(ctx.obj)

@C.command()
@C.pass_context
def read(ctx):
	"""read env vars from env config file"""
	ctx.obj=env.read(ctx.obj)




@C.command()
@C.pass_context
def start(ctx):
	"""start a new env for the current session"""
	ctx.obj = env.start(ctx.obj)



@C.command()
@C.pass_context
def write(ctx):
	"""write env config files"""
	ctx.obj=env.write(ctx.obj)



grp_env.add_command(create)
grp_env.add_command(read)
grp_env.add_command(start)
grp_env.add_command(write)


