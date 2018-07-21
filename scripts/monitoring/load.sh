#!/bin/bash
#Сравниваем la и количество ядер

cores=$(nproc)
avg5=$(cat /proc/loadavg |cut -d' ' -f1|sed 's/\.[0-9]*//g')
avg15=$(cat /proc/loadavg |cut -d' ' -f2|sed 's/\.[0-9]*//g')
if [ $avg5 -ge $cores ]
then
echo 'Повышенная нагрузка за последние 5 мин'
exit 1
elif [ $avg15 -ge $cores ]
then
echo 'Повышенная нагрузка за последние 15 мин'
exit 1
else
exit 0
fi