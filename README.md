# Linux Simple DDNS

Scripts (bash+python3) to dynamic update the linux /etc/hosts table, using a group os simplified scripts.

## The Method

The method is very simple, 

1. The new host put a udp message with his hostname over the subnet broadcast address
2. Other hosts that are at the same subnet, listen the message and process data to /etc/hosts tab. 

## Setup

1. Put all files at same folder ( "/opt/simple-dds" for example ).
2. Open the shell, goto the folder and run "./install.sh"
