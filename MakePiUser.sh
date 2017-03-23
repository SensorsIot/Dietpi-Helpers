#!/bin/bash
#
# ONLY use this script - as root - if user Pi does not exist on this device - to help with my main script, ROOT user can run this 
# (after adding execute permissions) to instantly make a user Pi with SUDO permissions and none of that constant password reminder stuff
# pi user will have password "password" - you should really change that ASAP. This script will run quickly and silently.
#
# So for Debian systems with no SUDO - add this first.
#
apt-get install -y sudo
#
# Now adding Pi user and ensuring they are part of the SUDO group - and minimising password requests
#
adduser --quiet --disabled-password --shell /bin/bash --home /home/pi --gecos "User" pi
echo "pi:password" | chpasswd
usermod pi -g sudo
echo "pi ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/pi
chmod 0440 /etc/sudoers.d/pi