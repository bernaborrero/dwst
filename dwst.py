# -*- coding: utf-8 -*-

import sys
import getopt
from downloader import Downloader

def main(arvg):
    show_status = False
    show_size = False
    wait_time = 5 # seconds to wait between requests

    if len(arvg) < 1:
        print_help()
        sys.exit(2)

    url = arvg[0]

    try:
        opts, _ = getopt.getopt(arvg[1:], 'hswt:')
    except getopt.GetoptError:
        print_help()
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h':
            print_help()
            sys.exit()
        elif opt == '-s':
            show_status = True
        elif opt == '-w':
            show_size = True
        elif opt == '-t':
            try:
                wait_time = float(arg)
            except ValueError:
                print 'Wait time must be an integer or a float'
                sys.exit(2)

    dwit = Downloader(url, show_status, show_size, wait_time)
    dwit.start()

def print_help():
    print "Dwst usage: python dwst.py url <options>\n"
    print "Options:"
    print "-s:\tShow response status (Default: False)"
    print "-w:\tShow response size (Default: False)"
    print "-t <x>:\tMake request every x seconds (Default: 5 seconds)"
    print "-h:\tShow this help"

if __name__ == '__main__':
    main(sys.argv[1:])
