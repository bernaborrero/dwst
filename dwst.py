# -*- coding: utf-8 -*-

import sys
import getopt
from downloader import Downloader

def main(arvg):
    show_status = False
    show_size = False
    show_redirections = False
    wait_time = 5 # seconds to wait between requests
    tries = -1 # number of requests (-1 corresponds to infinite)
    timeout = 10 # seconts to wait for host response

    if len(arvg) < 1:
        print_help()
        sys.exit(2)

    url = arvg[0]

    try:
        opts, _ = getopt.getopt(arvg[1:], 'hswrt:n:l:')
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
        elif opt == '-r':
            show_redirections = True
        elif opt == '-t':
            try:
                wait_time = float(arg)
            except ValueError:
                print('Wait time must be an integer or a float')
                sys.exit(2)
        elif opt == '-n':
            try:
                tries = int(arg)
            except ValueError:
                print('Number of tries must be an integer')
                sys.exit(2)
        elif opt == '-l':
            try:
                timeout = float(arg)
            except ValueError:
                print('Timeout time must be an integer or a float')
                sys.exit(2)

    options = {
        'show_status': show_status,
        'show_size': show_size,
        'show_redirections': show_redirections,
        'wait_time': wait_time,
        'tries': tries,
        'timeout': timeout
    }

    dwit = Downloader(url, options)
    dwit.start()

def print_help():
    print("Dwst usage: python dwst.py url <options>\n")
    print("Options:")
    print("-s:\tShow response status (Default: False)")
    print("-w:\tShow response size (Default: False)")
    print("-r:\tShow redirections (Default: False)")
    print("-t <x>:\tMake request every <x> seconds (Default: 5 seconds)")
    print("-n <n>:\tMake <n> number of requests (Default: no limit)")
    print("-l <l>:\tTimeout request after <l> seconds")
    print("-h:\tShow this help")

if __name__ == '__main__':
    main(sys.argv[1:])
