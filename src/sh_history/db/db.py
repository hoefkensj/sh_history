#!/usr/bin/env python
import click as C
from subprocess import getoutput
from sh_history.bash.env import getvar
from pathlib import Path
from Clict import Clict,Clict_from
import sqlite3
conn= sqlite3.connect('')
c= conn.cursor()
c.execute('INSERT INTO SEQRECORDS VALUES ('')')
SQLREC=Clict()
SQLREC.TIME_UNIX=int()
SQLREC.TIME_HUMAN=str()
SQLREC.TIME_BOOT=str()
SQLREC.MD5=str()
SQLREC.DOMAIN=str()
SQLREC.HOST=str()
SQLREC.USER=str()
SQLREC.OS=str()
SQLREC.TTY=str()
SQLREC.SHELL=str()
SQLREC.PID=int()
SQLREC.WORKINGDIR=str()
SQLREC.EXITCODE=int()
SQLREC.COMMAND=str()


c.execute(("SELECT * FROM SEQRECORDS"))


conn.commit()
conn.close()


'''
CREATE TABLE "record_fields" (
	"idx"	INTEGER UNIQUE,
	"V1_field"	TEXT,
	"V1_type"	TEXT,
	"V1_hash"	INTEGER,
	PRIMARY KEY("idx" AUTOINCREMENT)
)
'''







# def dict_to_sql_create_table(T):
# 	# Start the SQL statement with the CREATE TABLE clause
# 	TB=Clict()
# 	TB.filds=[]
# 	TB.PK=None
# 	for col in T:
# 		val=T[col]
# 		if col[0]=='*':col:=TB.PK=col[1:]
# 		f=Clict()
# 		f.keystr=f'"{col.upper()}"'
# 		val=val.split(',')
# 		if '++' in val:
#
# 		fields+=[f]
#
#
# 	# Process each column and its definition
# 	for key in sect:
#
# 			# Add the column definition
# 			sql_statement += f'\t"{column}"\t\t\t{definition},\n'
#
# 	# Remove the trailing comma and newline, then close the statement with a parenthesis
# 	sql_statement = sql_statement.rstrip(',\n') + '\n);'
#
# 	return sql_statement
#
#
# def meta():
# 	p=Path('dbtable.conf')
# 	sqltables=Clict_from.config(p)
# 	print(sqltables.hash_versions)
# 	for table in sqltables:
# 		sql_create_statement = dict_to_sql_create_table(table, sqltables[table])
# 		print(sql_create_statement)
# meta()

# id=C.obj.meta.id
	# META_ID = int(getoutput(f'cat {getvar(C,"sysfull"")} |wc -l'))	+1
	# META_TIME = "$TIMESTAMP"
	# META_BOOT = "$(bash_bootstamp)"
	# META_PID = "$$"
	# META_DISTRO = '{NAME}-{VERS}'.format(NAME=getoutput('source /etc/lsb-release && echo {VAR}'.format(VAR='"$DISTRIB_ID"')),VERS=getoutput('source /etc/lsb-release && echo {VAR}'.format(VAR='"$VERSION_ID"')))
	# META_TTY = "$(tty)"
	# META_BIN = "$SHELL"
	# META_DIR = "$PWD"
	# META_MD5 = "$( bash_history_md5 )"
	#
	# CSV = "${META_ID},${META_TIME},${META_MD5},${META_BOOT},${META_PID},${META_DISTRO},${META_HOST},${META_USR},${META_TTY},${META_BIN},${META_DIR},'${QCMD}'"
	#
	#
	#
	# META_HOST = "$HOSTNAME"
	# META_USR = "$(whoami)"

#
#
# 	CREATE TABLE "record-versions" (
# 	"id"	INTEGER UNIQUE,
# 	"name"	TEXT,
# 	"string" TEXT UNIQUE,
# 	"e"	TEXT,
# 	"m"	TEXT,
# 	"u"	TEXT,
# 	"n"	TEXT,
# 	"fields"	BLOB,
# 	"md5"	BLOB,
# 	"boot"	BLOB,
# 	"os"	BLOB,
# 	"host"	BLOB,
# 	"command"	INTEGER,
# 	PRIMARY KEY("id" AUTOINCREMENT)
# 	)
# CREATE TABLE "hash-versions" (
# 	"id"	INTEGER UNIQUE,
# 	"name"	TEXT,
# 	"string"	TEXT UNIQUE,
# 	"e"	INTEGER,
# 	"m"	INTEGER,
# 	"u"	INTEGER,
# 	"n"	INTEGER,
# 	"fields"	TEXT,
# 	"TIMESTAMP"	TEXT,
# 	"HOSTNAME"	TEXT,
# 	"USER"	TEXT,
# 	"CMD"	TEXT,
# 	PRIMARY KEY("id" AUTOINCREMENT)
# )
