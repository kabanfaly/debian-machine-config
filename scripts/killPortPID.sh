#!/usr/bin/env zsh
PORT=$1
kill -9 $(netstat -pln | grep $PORT | awk '{print $7}' | cut -d '/' -f 1)

