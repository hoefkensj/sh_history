#!/usr/bin/env python
import click as C
from sh_history.ui.cli.bash.env import grp_env
from sh_history.ui.cli.bash.vars import grp_vars
from sh_history.ui.cli.bash.file import grp_file
from sh_history.ui.cli.bash.append import cmd_append
from sh_history.bash.main import show


@C.group()
@C.pass_context
def bash_entry_point(ctx):
    """	help bash entrypoint"""
    pass



@C.command()
@C.pass_context
def cmd_show(ctx):
    """print out the full configuration"""
    ctx.obj=show(ctx.obj)
    print(repr(ctx.obj))

bash_entry_point.add_command(cmd_append,name='append')
bash_entry_point.add_command(grp_env,name='env',)
bash_entry_point.add_command(grp_file,name='file')
bash_entry_point.add_command(grp_vars,name='vars')
bash_entry_point.add_command(cmd_show,name='show')
