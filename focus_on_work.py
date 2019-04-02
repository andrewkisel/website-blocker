#! /usr/bin/python3

from datetime import datetime as dt
from traceback import format_exc
import time
import sys
import os

"""Simple script to run on your PC/Mac/Linux to block some of the distracting websites during working hours.
It does so by making modifications to 'hosts' file. If something goes wrong you should be able to restore
the original version of the file from the 'hosts_bckup' file stored in the same directory as your hosts.
However, in case of any exception/keyboard interruption the script should overwrite the hosts file with the info
it initially had in it and delete the backup file like it never existed.
Working hours are set by START_TIME and END_TIME variables using 24 hour format. Redirect URL/IP is set
using REDIRECT_URL variable. 
By default the script is configured to run on weekdays only. To run it on your machine, simply schedule it
to run at the startup"""

# List of websites to block.
TO_BLOCK = ['youtube.com', 'www.youtube.com', 'facebook.com', 'www.facebook.com', 'vk.com', 'www.vk.com',
            'mail.google.com', 'www.mail.google.com', 'calendar.google.com', 'www.calendar.google.com',
            'amazon.com', 'www.amazon.com']

# Redirect URL.
REDIRECT_IP = '127.0.0.1'

# Working hours.
START_TIME = 8
END_TIME = 17

# Determine where to look for hosts file depending on the OS,
if sys.platform in ['darwin', 'linux']:
    hosts_path = '/etc/hosts'
else:
    hosts_path = 'C:\\Windows\\System32\\drivers\\etc\\hosts'

# Making the backup file out of hosts.
hosts_file = open(hosts_path, 'r')
# Saving contents of the initial hosts file to this variable.
hosts_content = hosts_file.read()
backup_path = os.path.join(hosts_path.rstrip('hosts'), 'hosts_bckup')
hosts_bckup = open(backup_path, 'w')
hosts_bckup.write(hosts_content)
hosts_bckup.close()
hosts_file.close()


# Function to handle work with files.
def blocker():
    while True:
        # Main condition which determines working hours.
        if all([START_TIME <= dt.now().time().hour < END_TIME, dt.now().weekday() in range(0, 4)]):
            with open(hosts_path, 'r+') as new_hosts:
                content = new_hosts.read()
                for website in TO_BLOCK:
                    if website in content:
                        pass
                    else:
                        new_hosts.write('\n%s\t%s' % (REDIRECT_IP, website))
        # In case outside of working hours.
        else:
            # Check if the file looks like from the start of the script.
            with open(hosts_path, 'r') as old_hosts:
                # Check if the hosts file has been changed.
                if hosts_content == old_hosts.read():
                    # If so - simply pass.
                    pass
                else:
                    # Otherwise restore the initial version of the file.
                    hosts_out = open(hosts_path, 'w')
                    hosts_out.write(hosts_content)
                    hosts_out.close()
        time.sleep(30)


# Entry point.
if __name__ == '__main__':
    try:
        blocker()
    # Some fallbacks.
    except KeyboardInterrupt:
        print('Interrupted...Restoring the initial version of hosts file...')
        with open(hosts_path, 'w') as hosts:
            hosts.write(hosts_content)
            os.remove(backup_path)
    except Exception as e:
        print(
            'Oops. Here what caused the script to fail: %s.\nRestoring the initial version of hosts file...'
            % format_exc(e))
        with open(hosts_path, 'w') as hosts:
            hosts.write(hosts_content)
            os.remove(backup_path)
