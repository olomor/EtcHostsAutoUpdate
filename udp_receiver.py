#!/usr/bin/env python3
import fileinput
import re
import socket
import sys

# -----
def stdout(message):
  if verbose:
    print(message)

# -----
def exists(search):
  global data
  for l0 in data:
    for l1 in l0.split():
      if l1 == search:
        return True
  return False

# -----
def getip(search):
  global data
  for e in [ x.split() for x in data ]:
    for e2 in e:
      if e2 == search:
        return e[0]
  return None

# -----
def erase(search):
  global data
  data0 = [ x for x in data if not re.match('^'+search+' ',x) ].copy()
  data1 = [ x for x in data0 if not re.match('.* '+search+'([.]|$)',x) ].copy()
  data = data1.copy()
  stdout('Erased')

# -----
def insert():
  global data
  data.append(hostIp+" "+hostShort+" "+hostFqdn)
  stdout('Inserted')

# -----
def upsert():
  global data, hostFqdn, hostShort, hostIp
  if not exists(hostShort) or not exists(hostFqdn):
    insert()
    return True
  else:
    if not getip(hostFqdn) == hostIp or not getip(hostShort) == hostIp :
      erase()
      insert()
      return True
  return False

# -----
def writefile():
  global file
  with open(file,'w') as f:
    for l in data:
      if not l == '\n':
        f.write(l+"\n")
  load()

# -----
def load():
  global data
  global file
  content = open(file,'r').readlines()
  data = content.copy()
  data = [ x.strip() for x in data if not x == '\n' ].copy()

# -----
def validate():
  global hostFqdn, hostShort, hostIp
  load()
  if countif(hostShort) > 1:
    erase(hostShort)
  if countif(hostIp) > 1:
    erase(hostIp)
  if upsert():
    writefile()
    stdout('Updated:'+hostIp+' '+hostShort+' '+hostFqdn)

# -----
def countif(search):
  global data
  return len([ x for x in data if re.match('.*'+search+'(.|$)',x) ])

# -----
file = '/etc/hosts'
port = 2164
try:
    if sys.argv[1] == '-v': verbose = True
    else: verbose = False
except:
    verbose = False
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.bind(('', port))
except:
   print('# bind error')
   sys.exit()

while True:
    udpdata, udpaddr = s.recvfrom(1024)
    hostFqdn = str(udpdata,'utf-8').strip()
    hostShort = hostFqdn.split('.')[0]
    hostIp = udpaddr[0].strip()
    stdout('Received: '+hostIp+' '+hostFqdn)
    validate()

s.close()
