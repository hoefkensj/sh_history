#!/usr/bin/env python
import click
import click as C
from Clict import Clict,Clict_from
from pathlib import Path
from sh_history.bash_history import env


@C.group()
@C.pass_context
def entry_point(ctx):
    """env help"""
    ctx = env.bootstamp(ctx)
    ctx = env.config(ctx)



@C.command()
@C.pass_context
def create(ctx):
    """create help"""
    ctx=env.create(ctx)
    C.echo(ctx.obj.env.varfile.path)

@C.command()
@C.pass_context
def read(ctx):
    """read help"""
    ctx=env.read(ctx)
    print(repr(ctx.obj))

@C.command()
@C.pass_context
def write(ctx):
    """write help"""
    ctx=env.read(ctx)
    ctx=env.write_metafile(ctx)


@C.command()
@C.pass_context
def sourcefile(ctx):
    """sourcefile help"""
    ctx = env.init(ctx)
    ctx = env.config(ctx)
    ctx=env.read(ctx)
    srcfile=env.getvar(ctx, 'varsfile')

    C.echo(srcfile.absolute())

@C.command()
@C.argument('var')
@C.pass_context
def printvar(ctx,var):
    """sourcefile help"""
    ctx = env.init(ctx)
    ctx = env.config(ctx)
    ctx = env.read(ctx)
    val=env.getvar(ctx, var)
    click.echo(val)


@C.command()
@C.pass_context
def list(ctx):
    """sourcefile help"""
    ctx = env.config(ctx)
    ctx = env.init(ctx)
    ctx = env.read(ctx)
    ctx = env.scope(ctx)
    C.echo(repr(ctx.obj.env))




entry_point.add_command(create)
entry_point.add_command(read)
entry_point.add_command(write)
entry_point.add_command(sourcefile)
entry_point.add_command(list)
entry_point.add_command(printvar,name='print')

