#!/bin/bash

supervisorctl status | if grep -q RUNNING; then
	logger RabbitMQ is running
	exit 1
else
	/usr/local/bin/notify-remote
	logger RabbitMQ has died
fi
