#!/usr/bin/env zsh

arg=$1
[ $arg = "start" ] && docker-compose down && docker-compose pull && docker-compose up -d
[ $arg = "stop" ] && docker-compose down
