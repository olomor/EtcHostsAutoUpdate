#!/bin/bash

# For Oracle Linux / CentOS / Fedora

dnf install -y socat python3 && {
cat <<EOF >/etc/cron.d/linux-simple-ddns
SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=root
* * * * * root $(pwd)/start.sh
* * * * * root $(pwd)/udp_sender.sh
EOF
echo -e "\n\n Scripts installed."
}

firewall-cmd --add-port=2164/udp
firewall-cmd --runtime-to-permanent
