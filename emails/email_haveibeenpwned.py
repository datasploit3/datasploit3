#!/usr/bin/env python

import base
import vault
import sys
import requests
import json
from termcolor import colored

# Control whether the module is enabled or not
ENABLED = False



def banner():
    print(colored(base.style.BOLD + '\n---> Checking breach status in HIBP (@troyhunt)\n' + base.style.END, 'blue'))


def main(email):
    req = requests.get("https://haveibeenpwned.com/api/v3/breachedaccount/%s" % (email), headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36"})
    if req.status_code == 404:
        return {}
    print("CONtents:{0}".format(req.content))
    if 'Attention Required! | CloudFlare' in req.content:
        print("CloudFlare detected")
        return {}
    if req.content != "":
        try:
            return json.loads(req.content)
        except:
            return {}
    else:
        return {}


def output(data, email=""):
    if data:
        print(colored("Pwned at %s Instances\n", 'green') % len(data))
        for x in data:
            print("Title: %s\nBreachDate: %s\nPwnCount: %s\nDescription: %s\nDataClasses: %s\n" % (
                x.get('Title', ''), x.get('BreachDate', ''), x.get('PwnCount', ''), x.get('Description', ''),
                ", ".join(x.get('DataClasses', []))))
    else:
        print(colored("[-] No breach status found.", 'red'))


if __name__ == "__main__":
    try:
        email = sys.argv[1]
        banner()
        result = main(email)
        output(result, email)
    except Exception as e:
        print(e)
        print("Please provide an email as argument")
