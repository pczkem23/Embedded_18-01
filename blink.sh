#bin/bash

while((1)); do
	echo 1 > /sys/class/gpio/gpio21/value
	sleep 0.5 
	echo 0 > /sys/class/gpio/gpio21/value
	sleep 0.5
done
