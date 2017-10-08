# -*- encoding: utf-8 -*-

from time import sleep, time
import sys
from colorama import init
from termcolor import colored
import requests

class Downloader(object):
    headers = {'user-agent': 'dwst/1'}

    def __init__(self, url, show_status=False, show_size=False, wait_time=5):
        self.url = url
        self.show_status = show_status
        self.show_size = show_size
        self.wait_time = wait_time
        init(autoreset=True)    # init colorama

    def start(self):
        try:
            while True:
                init_time = time()
                web = requests.get(self.url, headers=self.headers)
                download_time = time() - init_time

                output = "%s downloaded in %s" % (self.url, download_time)
                if self.show_status:
                    output = output + "\tStatus: %s" % self.color_code(web.status_code)
                if self.show_size:
                    output = output + "\tSize: %s" % len(web.content)

                print output
                sleep(self.wait_time)
        except KeyboardInterrupt:
            sys.exit()
        except:
            raise

    def color_code(self, status_code):
        code_type = int(str(status_code)[:1])
        color = False

        if code_type == 1:
            color = 'blue'
        elif code_type == 2:
            color = 'green'
        elif code_type == 3:
            color = 'yellow'
        elif code_type == 4:
            color = 'red'
        elif code_type == 5:
            color = 'magenta'

        if color:
            return colored(status_code, color)
        else:
            return status_code
