#!/usr/bin/env python
import click as C
from sh_history.ui.cli import main

@C.group()
@C.pass_context
def entry_point(ctx,ui):
	"""	help ui"""
