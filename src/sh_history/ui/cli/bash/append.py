#!/usr/bin/env python
import click
import click as C
from pathlib import Path
from sh_history.bash_history import append

@C.command(name='append')
@C.pass_context
def entry_point(ctx):
	"""append help"""
	append.main(ctx)
