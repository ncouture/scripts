#!/bin/bash
#
# enable/disable yum by changing its configuration (/etc/yum.conf@plugins=0/1)
#
# Usage:
#        This script is intended to be executed as `yumon' and `yumoff', save it as `yumon' and
#        create a symbolic link to it as `yumoff'.
#
# nicolas.couture@gmail.com
#

name="$(basename $0)"

if [[ ! $(id -u) -eq 0 ]]; then
    echo "You must be root to run this script"
    exit 1
fi

if [[ "$name" == "yumon" ]]; then
    action="on"
elif [[ "$name" == "yumoff" ]]; then
    action="off"
else
    echo "This script must be called through 'yumon' or 'yumoff'" 
    exit 1
fi

if [[ "$action" == "on" ]]; then
    if grep ^"plugins=0" /etc/yum.conf &> /dev/null; then
	sed -i 's/^plugins=0/plugins=1/g' /etc/yum.conf
    else
	echo "Plugins are already enabled."
	exit 1
    fi
elif [[ "$action" == "off" ]]; then
    if grep ^"plugins=1" /etc/yum.conf &> /dev/null; then
	sed -i 's/^plugins=1/plugins=0/g' /etc/yum.conf
    else
	echo "Plugins are already disabled."
	exit 1
    fi
fi
