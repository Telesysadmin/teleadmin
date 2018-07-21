#!/bin/bash
# gcc -s -Wl,-Bstatic -lpython3.5m -I /usr/include/python3.5m teleadmin_wsgi.c
cp wsgi.py teleadmin_wsgi.pyx
cython teleadmin_wsgi.pyx --embed
gcc -s -Wl,-Bstatic -lpython3.5m -I /usr/include/python3.5m teleadmin_wsgi.c
#gcc -Os -I /usr/include/python3.5m -o teleadmin_wsgi teleadmin_wsgi.c -lpython3.5m -lpthread -lm -lutil -ldl