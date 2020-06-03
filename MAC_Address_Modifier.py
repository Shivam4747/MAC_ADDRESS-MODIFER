#!/usr/bin/env python

import subprocess
import optparse
from pyfiglet import Figlet


def modify_mac(interface, new_mac):
    print("[*] Modifying MAC_Address of " + interface + " to " + new_mac + "...\n")
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])
    print("\n[*] Restarting Network Services...\n")
    subprocess.call(['service', 'network-manager', 'restart'])
    print("\n[+] MAC_Address of " + interface + " has been successfully changed to " + new_mac + "\n")
    print("\n[+] Done")


def get_arguments():
    parser = optparse.OptionParser(usage='usage %prog [options] arguments')
    parser.add_option("-i", "--interface", dest="interface", help="Enter Interface Name")
    parser.add_option("-m", "--new-mac", dest="new_mac", help="Enter new MAC Address")
    parser.add_option("-s", action='store_true', help="Show Current MAC_Address(s)")
    (options, arguments) = parser.parse_args()
    if options.s:
        current_macs()
        exit(0)
    elif not options.interface:
        print("\n[-] Please specify Network Interface for the MAC to be changed! Use -h, --help, for more info!\n")
        exit(0)
    elif not options.new_mac:
        print("\n[-] Please specify New MAC_Address to change to! Use -h, --help, for more info!\n")
        exit(0)
    else:
        return options


def current_macs():
    print("\n[+] Current MAC_Address(s) of Network Interface(s) is/are follows: \n")
    subprocess.call("ip link | awk \'{print $2}\'", shell=True)
    print("\n[+] Done\n")


def text_render():
    print("\n\n----------------------MAC_Modifier Script made by----------------------\n")
    f = Figlet(font='slant')
    print(f.renderText('shIVam') + "\t\t\t\t\tv1.0\n\n\n")


def main():
    text_render()
    options = get_arguments()
    modify_mac(options.interface, options.new_mac)


if __name__ == '__main__':
    main()


