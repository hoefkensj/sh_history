#!/usr/bin/env python
#!/usr/bin/env python
import click as C
from sh_history.bash import env,vars

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
	ctx.obj = vars.setup(ctx.obj)
	ctx.obj = vars.dynamic(ctx.obj)
	C.echo(repr(ctx.obj.vars))

grp_vars.add_command(sourcefile)
grp_vars.add_command(listvars,name='list')
