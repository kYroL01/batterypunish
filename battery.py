#!/usr/bin/env python
#
# Michele Campus <michelecampus5@gmail.com>
# 
# encoding: utf-8
#
# Trigger an alert when battery status are low
#
# "batterypunish" is a python service to notify on the screen
# an alert message when the charge of battery is at 20 %
#
#
import gtk
import sys
import os.path
import time

#
# function to determine if power_supply use 
# charge_battery_props[] or energy_battery_props
#
def charge_or_energy():

    f = os.path.exists("/sys/class/power_supply/BAT0/charge_full")
    if(f):
        full = "/sys/class/power_supply/BAT0/charge_full"
    else:
        full = "/sys/class/power_supply/BAT0/energy_full"
        
    f = os.path.exists("/sys/class/power_supply/BAT0/charge_now")
    if(f):
        now = "/sys/class/power_supply/BAT0/charge_now"
    else:
        now = "/sys/class/power_supply/BAT0/energy_now"

    return (full, now)


#
# function to calculate the battery status (in percent)
# (located in BAT0 directory system)
#
def percent_battery_and_status():

    # call function to understand if the system use 'charge' or 'energy'
    full, now = charge_or_energy();

    s = "/sys/class/power_supply/BAT0/status"

    # read the file for full charge of the battery
    with open (full, "r") as myfile:
        max_charge = myfile.read()
        max_ch = float(max_charge)
        #print(max_charge)
    
    # read the file for current charge of the battery
    with open (now, "r") as myfile:
        curr = myfile.read()
        ch_now = float(curr)
        #print(ch_now)

    # read the file 'status' located in BAT0 directory system
    with open (s,"r") as myfile:
        status = myfile.read()
        #print(status)
            
    # calculate the real time percent of the battery
    percent = (ch_now / max_ch) * 100
    #print(percent)
    
    return (percent, status)


### PyAlert object class ###
class PyAlert(gtk.Window):
    def __init__(self):
        super(PyAlert, self).__init__()

        self.set_title("--- Battery LOW ---")
        self.set_size_request(350, 400)
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_icon_from_file("punicon.png")        

        img = gtk.Image()
        img.set_from_file("punicon.png")
        self.add(img)            
        
        self.connect("destroy", gtk.main_quit)
        self.show_all()


##
## MAIN
##
def main():

    loc = "/usr/share/pixmaps/punicon.png"
    b_status = "Discharging\n"
    lev_down_batt = 20.0
    chk = False
    Alert = PyAlert()

    # infinite loop
    while(True):

        # call function percent_battery - return batery percent and the status
        batt, status = percent_battery_and_status()

        # check status and level of battery charge
        if(status == b_status) and (batt <= lev_down_batt):
            if(chk == False):
                Alert
                gtk.main() # Trigger the gtk window
                chk = True
                
        # control every 10 seconds
        time.sleep(10)

    return 0


if __name__ == '__main__':main()
