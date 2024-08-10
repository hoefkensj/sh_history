#!/usr/bin/env python

import os,sys,re,platform
from pathlib import Path
from subprocess import getoutput
import click as C
from Clict import Clict,Clict_from

def config():
	configpath = Path(Path(__file__).parent, 'config')
	cfg= Clict_from.config(configpath)
	return cfg

def os_version():
	META_DISTRO = '{NAME}-{VERS}'.format(
		NAME=getoutput('source /etc/lsb-release && echo {VAR}'.format(VAR='"$DISTRIB_ID"')),
		VERS=getoutput('source /etc/lsb-release && echo {VAR}'.format(VAR='"$VERSION_ID"')))
def bootstamp():
	cmd="uptime -s | tr -d '\-: '"
	bootstamp=getoutput(cmd)
	return bootstamp

def parentPid():

	return ctx

def init(ctx):
	ctx.obj.env.bootstamp=bootstamp(ctx)
	ctx.obj.env.pid=os.getppid()
	ctx.obj.cfg.sys=config(ctx)
	cmd=ctx.obj.cfg.sys.cmds.VARS.HOSTNAME
	ctx.obj.env.hostname=getoutput(cmd)
	ctx.obj.state+=['init']
	return ctx

def load(ctx):
	ctx=init(ctx)
	cfgfile=ctx.obj.cfg.sys.paths.FILES.CONFFILE
	cfgfile=Path(cfgfile.format(**ctx.obj.env))
	done=0
	while not done:
		if cfgfile.exists():
			ctx=read(ctx)
			done=1
		else:
			ctx=init(ctx)
			ctx=create(ctx)


def create(ctx):
	# [print(k) for k in [*os.environ.keys()]]
	# print(repr(cfg))
	cfg=ctx.obj.cfg.sys
	F = cfg.paths.FOLDERS
	f = cfg.paths.FILES
	tplvar = 'BASH_HIST_{TYPE}_{KEY}'
	tplexp = 'export {KEY}="{VAL}"\n'
	tplcfg = 'BASH_{KEY} : {VAL}\n'
	tplfil = '{KEY} : {VAL}\n'
	str_varfile = ''
	str_conffile='[HISTDIRS]\n'
	vars = []
	ctx=bootstamp(ctx)
	for FF in F:
		bvar = tplvar.format(TYPE='DIR', KEY=FF)
		bdir = Path(F[FF].format(**ctx.obj.env))
		ctx.obj.env.hist.dir[FF.lower()].key=FF
		ctx.obj.env.hist.dir[FF.lower()].val=bdir
		ctx.obj.env.hist.dir[FF.lower()].var=bvar
		ctx.obj.env.hist.dir[FF.lower()].exp=tplexp.format(KEY=bvar,VAL=bdir)
		ctx.obj.env.hist.dir[FF.lower()].cfg=tplcfg.format(KEY=FF,VAL=bdir)
		bdir.mkdir(parents=True, exist_ok=True, mode=0o777)

	for ff in f:
		bvar = tplvar.format(TYPE='FILE', KEY=ff)
		bfil = Path(f[ff].format(**ctx.obj.env))
		ctx.obj.env.hist.file[ff.lower()].key=ff
		ctx.obj.env.hist.file[ff.lower()].val=bfil
		ctx.obj.env.hist.file[ff.lower()].var=bvar
		ctx.obj.env.hist.file[ff.lower()].exp=tplexp.format(KEY=bvar,VAL=bfil)
		ctx.obj.env.hist.file[ff.lower()].cfg=tplcfg.format(KEY=ff,VAL=bfil)
		bfil.touch(exist_ok=True, mode=0o777)

	for file,k in zip(['var','cfg','hist'],['varsfile','conffile','histfile']):
		file=f'{file}file'
		ctx.obj.env.file[file].key=file.upper()
		ctx.obj.env.file[file].val=ctx.obj.env.hist.file[k].val
		ctx.obj.env.file[file].exp = tplexp.format(KEY=k.upper(), VAL=ctx.obj.env.hist.file[k].val)
		ctx.obj.env.file[file].cfg = tplfil.format(KEY=k.upper(), VAL=ctx.obj.env.hist.file[k].val)
	# ctx.obj.env.hist.vars.bootstamp.bexp=tplexp.format(KEY='BASH_HIST_BOOTSTAMP',VAL=ctx.obj.env.bootstamp)
	ctx.obj.state+=['create']
	return ctx

def read(ctx):
	pid=ctx.obj.env.pid
	cfgfile=ctx.obj.cfg.sys.paths.FILES.CONFFILE
	ctx.obj.env.cfgfile=cfgfile.format(**ctx.obj.env)
	ctx.obj.env.read=Clict_from.config(ctx.obj.env.cfgfile)
	for ptype in ctx.obj.env.read:
		for key in ctx.obj.env.read[ptype]:
			ctx.obj.env.hist[ptype[4:]][key]=Path(ctx.obj.env.read[ptype][key])
			if not key.startswith('BASH'):
				ctx.obj.env[key]=Path(ctx.obj.env.read[ptype][key])

	return ctx
def scope(ctx):
	pid=ctx.obj.env.pid
	for ptype in ctx.obj.env.read:
		for key in ctx.obj.env.read[ptype]:
			skey = key.removeprefix(f'{ctx.obj.env.shell}_'.upper()).lower()
			ctx.obj.scope[skey] = Path(ctx.obj.env.read[ptype][key])
	ctx.obj.env.scope=ctx.obj.scope
	return ctx



def getvar(ctx, var):
	def descend(dct,var):
		result=None
		ret=None
		for item in dct:
			if isinstance(dct[item], dict):
				result = descend(dct[item], var)
			if item.casefold()==var.casefold() or item.casefold()==f'{ctx.obj.env.shell}_{var}':
				result=dct[item]
				if isinstance(dct[item],dict):
					if 'val' in dct[item]:
						result=dct[item].val

			if result:
				ret=result
		return ret
	val=descend(ctx.obj,var)
	return val

def write_envfiles(ctx):
	metastr='#!/usr/bin/env bash\n'
	confstr=''
	env=ctx.obj.env.hist

	for TYPE in env:
		confstr+=f'[HIST{TYPE.upper()}S]\n'
		for KEY in env[TYPE]:
			metastr+= env[TYPE][KEY.lower()].exp
			confstr+= env[TYPE][KEY.lower()].cfg
	for file in ctx.obj.env.file:
		metastr += ctx.obj.env.file[file].exp
		confstr += ctx.obj.env.file[file].cfg

	with open(ctx.obj.env.file.varfile.val, 'w') as v:
		v.write(metastr)

	with open(ctx.obj.env.file.cfgfile.val, 'w') as v:
		v.write(confstr)

def printvar(ctx,var):
	return ctx.obj.env.hist.get(var)


