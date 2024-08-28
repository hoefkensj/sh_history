#!/usr/bin/env python
#!/usr/bin/env python
import click as C
from Clict import Clict,Clict_from
from pathlib import Path
from sh_history.bash import env
import sys,os
from sh_history.tools import shell

@C.group()
@C.pass_context
def grp_vars(ctx):
	"""env help"""
	pass


@C.command()
@C.pass_context
def sourcefile(ctx):
	"""sourcefile help"""
	ctx = env.init(ctx)
	ctx=env.read(ctx)
	srcfile=env.getvar(ctx, 'varsfile')
	C.echo(f'BASH_HIST_FILE_VARSFILE="{srcfile.absolute()}"')





@C.command()
@C.pass_context
def listvars(ctx):
    """sourcefile help"""
    ctx.obj = env.init(ctx.obj)
    ctx.obj = env.load(ctx.obj)
    ctx.obj = env.read(ctx.obj)
    ctx.obj = env.scope(ctx.obj)

    C.echo(repr(ctx.obj.env))


@C.command()
@C.pass_context
def cleanvars(ctx):
    """cleanvars help"""
    ctx = env.init(ctx)
    ctx = env.load(ctx)
    ctx = env.scope(ctx)
    # C.echo(ctx.obj.env.clean.unset)
grp_vars.add_command(cleanvars)
grp_vars.add_command(sourcefile)
grp_vars.add_command(listvars,name='list')
