#!/bin/bash
cd "$(dirname $0)"
ps -eo pid,cmd |grep -v grep |grep '/bin/python3 udp_receiver.py' || {
  nohup /bin/python3 udp_receiver.py &
}
