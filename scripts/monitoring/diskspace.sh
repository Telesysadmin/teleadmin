#!/bin/bash
#проверяем место на сервере
echo "check diskspace"
df=`df -h | grep vda2 | awk '{print $5}' | sed 's/%//'`
if [ $df -gt 95 ]
then
	echo "На сервере 188.120.234.35 заканчивается место, сейчас занято $df %"
	exit 1
fi