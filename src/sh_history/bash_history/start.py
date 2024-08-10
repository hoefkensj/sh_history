#!/usr/bin/env python
from sh_history.bash_history import env
from sh_history.bash_history.main import load

from pathlib import Path
def main(ctx):
	ctx=env.init(ctx)
	ctx=env.create(ctx)
	env.write_envfiles(ctx)
	# ctx=load(ctx)
	# pid=ctx.obj.env.pid
	# [exec(string) for string in ctx.obj.scope[pid].strs]
	return ctx


from Clict import Clict
db=Clict()
#
# h.id
# h.version
# h.time
# h.md5
# h.boot
# h.pid
# h.os
# h.host
# h.user
# h.tty
# h.shell
# h.pwd
# h.command
# h.exit
# h.priv
# h.shared
# h.deleted
#
# db.versions
#
#
# db.hosts[HOST].shell[SHELL].history[TABLE]=table()
