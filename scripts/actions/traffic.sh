#!/bin/bash
iface=`awk '/iface/ && !/lo/ {print $2}' /etc/network/interfaces 2>/dev/null | awk 'NR == 1' || awk 'BEGIN {FS = "="} /DEVICE/ && !/lo/ {print $2}' /etc/sysconfig/network-scripts/ifcfg* | awk 'NR==1' 2>/dev/null`
rx1=`cat /sys/class/net/$iface/statistics/rx_bytes 2>/dev/null`
tx1=`cat /sys/class/net/$iface/statistics/tx_bytes 2>/dev/null`
sleep 1 #Нужно чтобы получить инфу по трафику
#rx2=`cat /sys/class/net/eth0/statistics/rx_bytes 2>/dev/null || cat /sys/devices/virtual/net/venet0/statistics/rx_bytes 2>/dev/null` && let rx=$rx2-$rx1 && let rx=$rx*8 && let rx=$rx/1024 2>/dev/null
#tx2=`cat /sys/class/net/eth0/statistics/tx_bytes 2>/dev/null || cat /sys/devices/virtual/net/venet0/statistics/tx_bytes 2>/dev/null` && let tx=$tx2-$tx1 && let tx=$tx*8 && let tx=$tx/1024 2>/dev/null
rx2=`cat /sys/class/net/$iface/statistics/rx_bytes 2>/dev/null` && let rx=$rx2-$rx1 && let rx=$rx*8 && let rx=$rx/1024 2>/dev/null
tx2=`cat /sys/class/net/$iface/statistics/tx_bytes 2>/dev/null` && let tx=$tx2-$tx1 && let tx=$tx*8 && let tx=$tx/1024 2>/dev/null
echo "network in: $rx Kbit/sec"
echo "network out: $tx Kbit/sec"
exit 0