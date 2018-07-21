#!/bin/bash
#Проверяем очередь процессов на сервере
LAd=`/usr/bin/w | grep average | awk '{print $10, $11, $12}' | sed 's/,//g'`
LA=(`echo $LAd | sed 's/\.//g'`)
if [ ${LA[0]} -gt 2000 ] || [ ${LA[1]} -gt 3000 ] || [ ${LA[2]} -gt 4000 ]
	then
		echo "На сервере 188.120.234.35 LA $LAd"
		echo `top -b -n 1 | grep Cpu`
		echo "Топ 5 процессов `top -b -n 1 | grep -A 5 'PID USER' | tail -5`"
		exit 1
	fi
