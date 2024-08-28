#!/usr/bin/env python
import click as C
from sh_history.bash import append
@C.command(name='append')
@C.pass_context
def cmd_append(ctx):
	"""append help"""
	append.main(ctx)
