#!/bin/sh
### BEGIN INIT INFO
# Provides: dnscheck
# Required-Start: $remote_fs $syslog
# Required-Stop: $remote_fs $syslog
# Default-Start: 2 3 4 5
# Default-Stop:  0 1 6
# Short-Description: Start fan script at boot time
# Description: Enable service provided by daemon.
### END INIT INFO
python /home/pi/Development/run-fan.py