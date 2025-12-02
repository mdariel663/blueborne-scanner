import os
import time
import bluetooth
from classes.deviceslist import devices

devicelookup = devices.get_devices()

def search():         
    print("searching for devices")
    try:
        devices = bluetooth.discover_devices(duration=20, lookup_names = True)
    except OSError as oserr:
        if oserr.errno == 19: # Not such device
            if os.getuid() == 0:
                print("device bluetooth not found. Try reconnect again!!!!")
            else:
                print("device bluetooth not found. Retry in root or with sudo")
        raise SystemExit(0)
    return devices

def is_device_vulnerable(addr):
    #print "looking up OUI {0}".format(addr[:8])

    manufacturers = devicelookup["ANDROIDS"]

    for manufacturer in manufacturers:
        #print manufacturer
        lookups = manufacturers[manufacturer]
        for _ in lookups:
            if _ == addr[:8]:
                return True
                #print "FOUND : " + _

    return False

if __name__=="__main__":

    print ("\n")
    print ("\x1b[1;35mhook's Blueborne Android scanner v0.01\x1b[0m")
    print ("\n")
    print ("\n")

    try:
        while True:        
            results = search()
            if (results!=None):
                for addr, name in results:
                    vulnerable = is_device_vulnerable(addr)
                    print("{0} - {1} - {isVulnerable}Vulnerable".format(addr, name, isVulnerable="!!! IS " if vulnerable else "NOT "))
                #endfor
            #endif
            time.sleep(60)
        #endwhile

    except KeyboardInterrupt:
        print ("\n\x1b[1;35m                             ")
        print ("    _    (^)                             ")
        print ("   (_\   |_|                             ")
        print ("    \_\  |_|                             ")
        print ("    _\_\,/_| ap0r                        ")
        print ("   (`\(_|`\|                             ")
        print ("  (`\,)  \ \'                            ")
        print ("   \,)   | |                             ")
        print ("     \__(__|\x1b[0m                      ")
        print ("                                         ")
        print ("Shoutz to sh3llg0d, an0n, daemochi, akatz")
        print ("Peace!                                   ")
        print ("\n                                       ")
