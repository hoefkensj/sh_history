#!/usr/bin/env python
import os,sys,re,platform
from pathlib import Path
from Clict import Clict,Clict_from

def load(ctx):
	from sh_history.bash_history import env
	ctx = env.config(ctx)
	ctx = env.init(ctx)
	ctx = env.read(ctx)
	logfile=env.getvar(ctx, 'BOOTLOG')
	ctx = env.scope(ctx)
	return ctx
