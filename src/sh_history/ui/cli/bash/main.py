#!/usr/bin/env python
import click as C
from sh_history.ui.cli.bash.env import grp_env
from sh_history.ui.cli.bash.vars import grp_vars
from sh_history.ui.cli.bash.file import grp_file
from sh_history.bash.append import append
from sh_history.tools import lastcmd,md5hash,getoutput

from sh_history.bash import env


@C.group()
@C.pass_context
def bash_entry_point(ctx):
    """	help bash entrypoint"""
    pass

@C.command()
@C.pass_context
def cmd_append(ctx):
    """append help"""
    append(ctx.obj)

@C.command()
@C.argument('command', default=None)
@C.pass_context
def cmd_hash(ctx,command):
    """append help"""
    ctx.obj.command=command
    ctx.obj = env.init(ctx.obj)

    ctx.obj = env.load(ctx.obj)
    ctx.obj = env.read(ctx.obj)
    ctx.obj = lastcmd(ctx.obj)
    ctx.obj.vars.time=getoutput('date +%s%9N') #way to late after command
    ctx.obj = md5hash(ctx.obj)
    print(ctx.obj.meta.hash)

@C.command()
@C.pass_context
def cmd_show(ctx):
    """print out the full configuration"""

    ctx.obj = env.init(ctx.obj)
    ctx.obj = env.load(ctx.obj)
    ctx.obj = env.read(ctx.obj)
    print(list(ctx.obj))

bash_entry_point.add_command(cmd_append,name='append')
bash_entry_point.add_command(grp_env,name='env',)
bash_entry_point.add_command(grp_file,name='file')
bash_entry_point.add_command(grp_vars,name='vars')
bash_entry_point.add_command(cmd_show,name='show')
bash_entry_point.add_command(cmd_hash,name='hash')
