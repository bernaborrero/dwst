# -*- encoding: utf-8 -*-

from time import sleep, time
import sys
import requests

class Downloader(object):
    headers = {'user-agent': 'dwst/1'}

    def __init__(self, url, show_status=False, show_size=False, wait_time=5):
        self.url = url
        self.show_status = show_status
        self.show_size = show_size
        self.wait_time = wait_time

    def start(self):
        try:
            while True:
                init_time = time()
                web = requests.get(self.url, headers=self.headers)
                download_time = time() - init_time

                output = "%s downloaded in %s" % (self.url, download_time)
                if self.show_status:
                    output = output + "\tStatus: %s" % web.status_code
                if self.show_size:
                    output = output + "\tSize: %s" % len(web.content)

                print output
                sleep(self.wait_time)
        except KeyboardInterrupt:
            sys.exit()
        except:
            raise