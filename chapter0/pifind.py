#!/usr/bin/env python2.7
import smtplib, string, subprocess
import os

os.system(" hostname -I | awk '{print $1;}' > .ipaddress.txt")
# Script to get IP Address while running a Raspberry Pi headless.
# pifind.py gets the system parameters you want to know and 
# emails them through gmail to a destination of your choice

# INSTALLING pifind
# Add this line to /etc/rc.local
#   python /home/pi/pifind.py
# And place this file, pifind.py in your /home/pi folder, then
#   sudo chmod 755 /home/pi/pifind.py

# Settings
#When editing these lines, remove the <>, but not the quotes
fromaddr = 'robert.schreibman@gmail.com' #'<insert from addr here>'  
toaddr  = 'robert.schreibman@gmail.com' #'<insert any email addr you have access to>'  

# Googlemail login details
username = 'robert.schreibman' #'<your username for the gmail account without @gmail.com>'  
password = 'imnotsure18' #'<the password for that account>'  

output_if = subprocess.Popen(['ifconfig'], stdout=subprocess.PIPE).communicate()[0]
#output_cpu = open('/proc/cpuinfo', 'r').read()
output_ip = open('.ipaddress.txt', 'r').read()

BODY = string.join((
        "From: %s" % fromaddr,
        "To: %s" % toaddr,
        #"Subject: Your RasPi just booted",
        "Subject: RasPi {}".format(output_ip),
        "",
        output_if,
        #output_cpu,
        ), "\r\n")
      
# send the email  
server = smtplib.SMTP('smtp.gmail.com:587')  
server.starttls()  
server.login(username,password)  
server.sendmail(fromaddr, toaddr, BODY)  
server.quit()

