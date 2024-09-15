#!/usr/bin/env python

import os
from pathlib import Path
from Clict import Clict_from

import sh_history.bash.vars
from sh_history.bash.vars import dynamic,setup


def config():
	configpath = Path(Path(__file__).parent, 'config')
	cfg= Clict_from.config(configpath)
	return cfg


def start(C):
	C=init(C)
	C=create(C)
	C=write(C)
	C.state+=['start']

	return C
def init(C):
	C= setup(C)
	C= dynamic(C)
	C.sys.conf=config()
	C.state+=['init']
	return C



def create(C):
	env=C.env
	# [print(k) for k in [*os.environ.keys()]]
	# print(repr(cfg))
	cfg=C.sys.conf
	paths=cfg['paths']
	F = paths.FOLDERS
	f = paths.FILES
	D = paths.CLEAN
	tplvar = 'BASH_HIST_{TYPE}_{KEY}'
	tplexp = 'export {KEY}="{VAL}"\n'
	tplcfg = 'BASH_{KEY} : {VAL}\n'
	tplfil = '{KEY} : {VAL}\n'
	str_varfile = ''
	str_conffile='[HISTDIRS]\n'
	vars = []
	for FF in F:
		bvar = tplvar.format(TYPE='DIR', KEY=FF)
		bdir = Path(F[FF].format(**C.vars))
		env.created.dir[FF.lower()].key=FF
		env.created.dir[FF.lower()].val=bdir
		env.created.dir[FF.lower()].var=bvar
		env.created.dir[FF.lower()].exp=tplexp.format(KEY=bvar,VAL=bdir)
		env.created.dir[FF.lower()].cfg=tplcfg.format(KEY=FF,VAL=bdir)
		bdir.mkdir(parents=True, exist_ok=True, mode=0o777)

	for ff in f:
		bvar = tplvar.format(TYPE='FILE', KEY=ff)
		bfil = Path(f[ff].format(**C.vars))
		env.created.file[ff.lower()].key=ff
		env.created.file[ff.lower()].val=bfil
		env.created.file[ff.lower()].var=bvar
		env.created.file[ff.lower()].exp=tplexp.format(KEY=bvar,VAL=bfil)
		env.created.file[ff.lower()].cfg=tplcfg.format(KEY=ff,VAL=bfil)

	for file,k in zip(['var','cfg','hist'],['varsfile','conffile','histfile']):
		file=f'{file}file'
		env.file[file].key=file.upper()
		env.file[file].val=env.created.file[k].val
		env.file[file].exp = tplexp.format(KEY=k.upper(), VAL=env.created.file[k].val)
		env.file[file].cfg = tplfil.format(KEY=k.upper(), VAL=env.created.file[k].val)

	env.clean.unset=D.UNSET.split(',')
	env.clean.delete=D.DELETE.split(',')

	C.state+=['create']
	return C



def write(C):

	metastr='#!/usr/bin/env bash\n'
	confstr=''
	env=C.env.created
	efile=C.env.file

	for TYPE in env:
		confstr+=f'[HIST{TYPE.upper()}S]\n'
		for KEY in env[TYPE]:
			metastr+= env[TYPE][KEY.lower()].exp
			confstr+= env[TYPE][KEY.lower()].cfg
	for file in efile:
		metastr += efile[file].exp
		confstr += efile[file].cfg
	metastr+='BASH_HIST_UNSET_VARS="{VARS}"\n'.format(VARS=' '.join(C.env.clean.unset))
	# print(f'writing {efile.varfile.val}...')
	with open(efile.varfile.val, 'w') as v:
		v.write(metastr)
	# print(f'writing {C.env.file.cfgfile.val}...')
	with open(efile.cfgfile.val, 'w') as v:
		v.write(confstr)
	C.written.file.bash=C.env.file.varfile.val
	C.written.file.conf=C.env.file.cfgfile.val
	C.state+=['write']
	return C


def load(C):
	cfgfile=C.sys.conf.paths.FILES.CONFFILE
	cfgfile=Path(cfgfile.format(**C.vars))
	C.sys.load = Clict_from.config(cfgfile)
	if not cfgfile.exists():
		breakpoint()
	C.state+=['load']

	return C

def read(C):
	pid=C.vars.pid
	for ptype in C.sys.load:
		for key in C.sys.load[ptype]:
			C.env.read[ptype[4:]][key]=Path(C.sys.load[ptype][key])
			if not key.startswith('BASH'):
				C[key]=Path(C.sys.load[ptype][key])

	C.state+=['read']
	return C



