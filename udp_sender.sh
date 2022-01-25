#!/bin/bash
BROADCAST="$(ip address show eth0 |grep ' inet ' |awk '{print $4}')"
hostname | socat - udp-datagram:${BROADCAST}:2164,broadcast && {
  echo "hostname ${HOSTNAME} sent to broadcast $BROADCAST udp 2164"
}
