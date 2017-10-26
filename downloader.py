# -*- encoding: utf-8 -*-

from time import sleep, time
import sys
from colorama import init
from termcolor import colored
import requests

class Downloader(object):
    headers = {'user-agent': 'dwst/1'}

    def __init__(self, url, show_status=False, show_size=False, show_redirections=False, wait_time=5, tries=-1, timeout=10):
        self.url = url
        self.show_status = show_status
        self.show_size = show_size
        self.show_redirections = show_redirections
        self.wait_time = wait_time
        self.tries = tries
        self.timeout = timeout
        init(autoreset=True)    # init colorama

    def start(self):
        current_tries = 0
        downloader_init_time = time()
        try:
            while self.tries < 0 or current_tries < self.tries:
                if current_tries > 0:
                    sleep(self.wait_time)

                init_time = time()
                try:
                    web = requests.get(self.url, headers=self.headers, timeout=self.timeout)
                    download_time = time() - init_time
                    print self.format_output(download_time, web.status_code, len(web.content), web.history)
                except requests.exceptions.Timeout:
                    print "%s timed out" % self.url
                except requests.exceptions.TooManyRedirects:
                    print "%s exceeded the max number of redirects allowed" % self.url
                except requests.exceptions.ConnectionError:
                    print "%s connection failed" % self.url

                current_tries = current_tries + 1
            self.end(current_tries, downloader_init_time)
        except KeyboardInterrupt:
            self.end(current_tries, downloader_init_time)
        except:
            raise

    def format_output(self, download_time, status_code, content_length, history):
        output = "%s downloaded in %s sec" % (self.url, download_time)
        if self.show_status:
            output = output + "\tStatus: %s" % self.color_code(status_code)
        if self.show_size:
            output = output + "\tSize: %s KB" % (content_length / 1024)
        if self.show_redirections:
            if len(history) > 1:
                redirections = []
                for step in history:
                    redirections.append(step.url)
                output = output + "\t[" + ', '.join(redirections) + ']'
        return output

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
    
    def print_summary(self, current_tries, elapsed_time):
        print "Done. %s tries in %s seconds." % (current_tries, elapsed_time)

    def end(self, current_tries, downloader_init_time):
        self.print_summary(current_tries, time() - downloader_init_time)
        sys.exit()