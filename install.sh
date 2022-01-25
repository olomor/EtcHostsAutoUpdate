#!/bin/bash

dnf install -y socat ipcalc python3 && {
cat <<EOF >/etc/cron.d/etc-hosts-autoupdate
* * * * * root "/root/scripts/EtcHostsAutoUpdate/start.sh"
* * * * * root "/root/scripts/EtcHostsAutoUpdate/udp_sender.sh"
EOF
echo -e "\n\n Scripts installed."
}

firewall-cmd --add-port=2164/udp
firewall-cmd --runtime-to-permanent
