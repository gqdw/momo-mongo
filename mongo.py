import pymongo
import sys
from pymongo import MongoClient
#argv[1] ip
#argv[2] port
#argv[3] opt
#print type(sys.argv[2])
client = MongoClient(sys.argv[1], int(sys.argv[2]))
db = client.admin
c = db.command('serverStatus')
if sys.argv[3] == 'insert':
	print c['opcounters']['insert']
elif sys.argv[3] == 'update':
	print c['opcounters']['update']
elif sys.argv[3] == 'query':
	print c['opcounters']['query']
elif sys.argv[3] == 'getmore':
	print c['opcounters']['getmore']
elif sys.argv[3] == 'command':
	print c['opcounters']['command']
elif sys.argv[3] == 'delete':
	print c['opcounters']['delete']
elif sys.argv[3] == 'networkin':
	print c['network']['bytesIn']
elif sys.argv[3] == 'networkout':
	print c['network']['bytesOut']
elif sys.argv[3] == 'backgroundFlushing':
	print c['backgroundFlushing']['average_ms']
elif sys.argv[3] == 'connections':
	print c['connections']['current']
elif sys.argv[3] == 'virtual':
	print c['mem']['virtual']
elif sys.argv[3] == 'resident':
	print c['mem']['resident']
elif sys.argv[3] == 'repl-hosts':
	print len(c['repl']['hosts'])
else:
	print 'something wrong'
