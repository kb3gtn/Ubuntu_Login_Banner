#!/bin/bash
echo "Installing pop up banner.  To disable, edit /usr/share/lightdm/lightdm.conf.d/50-ubuntu.conf" 
sudo cp /usr/share/lightdm/lightdm.conf.d/50-ubuntu.conf /usr/share/lightdm/lightdm.conf.d/50-ubuntu.backup
sudo cp 50-ubuntu.conf /usr/share/lightdm/lightdm.conf.d/50-ubuntu.conf
sudo cp login_banner.html /etc/
sudo cp banner_popup_pyqt5.py /usr/bin
echo "Reboot for banner to take effect.."

