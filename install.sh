#!/bin/bash
if [ -x ./login_popup/login_popup ]; then
	echo "Installing pop up banner.  To disable, edit /usr/share/lightdm/lightdm.conf.d/50-ubuntu.conf" 
	sudo cp /usr/share/lightdm/lightdm.conf.d/50-ubuntu.conf /usr/share/lightdm/lightdm.conf.d/50-ubuntu.backup
	sudo cp 50-ubuntu.conf /usr/share/lightdm/lightdm.conf.d/50-ubuntu.conf
	sudo cp login_banner.html /etc/
	sudo cp login_popup/login_popup /usr/bin
	echo "Reboot for banner to take effect.."
else
	echo "You need to build the login_pop program first.."
	echo "install qtcreator, then cd into the login_popup directory and run qmake && make"
fi

