#!/usr/bin/env python
import click as C
@C.group()
@C.pass_context
def entry_point(ctx):
    """	help bash entrypoint"""

    from sh_history.bash_history import env
    ctx.obj.env.shell='bash'
    ctx = env.init(ctx)




@C.command()
@C.pass_context
def env(ctx):
    """env help"""
    pass


@C.command()
@C.pass_context
def start(ctx):
    """env help"""
    pass

@C.command()
@C.pass_context
def append(ctx):
    """append help"""
    pass
from sh_history.ui.cli.bash import env
from sh_history.ui.cli.bash import start
from sh_history.ui.cli.bash import append

entry_point.add_command(env.entry_point,name='env')
entry_point.add_command(start.entry_point,name='start')
entry_point.add_command(append.entry_point,name='append')
