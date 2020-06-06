#!/usr/bin/env python

import urllib.request, urllib.error
import json
import os
import platform
import argparse
import datetime

def open_browser(url):
    platform_name = platform.system()
    if platform_name == 'Darwin':
        os.system('open ' + url)
    elif platform_name == 'Windows':
        os.system('start ' + url)
    else:
        print("TBD")

def open(redmine_url, issues, expired_time=None):
    for issue in issues:
        issue_url = redmine_url + "issues/" + str(issue['id'])
        if (expired_time):
            if ('due_date' not in issue):
                continue;
            due_datetime = datetime.datetime.strptime(str(issue['due_date']), '%Y-%m-%d')
            if (due_datetime < datetime.datetime.today()):
                open_browser(issue_url)
        else:
            open_browser(issue_url)

def list(issues):
    for issue in issues:
        print(str(issue['id']) + " " + issue['subject'] + " " + issue['status']['name'])

def rto_main():
    parser = argparse.ArgumentParser(description="option")
    parser.add_argument('-a', action="store", type=str, default="open", dest='action',
        help='open is opening issue url in browser, list is printing commandline.default is open')
    parser.add_argument('-et', action='store_true', default=False, dest='expired_time',
        help='open issue of over due time')
    parser.add_argument('-p', action='store', default="", dest='project_id',
        help='open issue of directed project.')
    args = parser.parse_args()

    try:
        redmine_url = os.environ['REDMINE_URL']
    except:
        print("you should set REDMINE_URL environment variable.")
        return

    if redmine_url[-1] != '/':
        redmine_url += '/'

    try:
        api_key = os.environ['REDMINE_API_KEY']
    except:
        print("you should set REDMINE_API_KEY environment variable.")
        return

    rest_url = redmine_url + 'issues.json?key=' + api_key + '&status_id=open&assigned_to_id=me'
    if args.project_id != "":
        rest_url += '&project_id=' + args.project_id
    req = urllib.request.Request(rest_url)
    try:
        res = urllib.request.urlopen(req)
        ret = res.read()
    except urllib.error.HTTPError as e:
        print(e)
        return

    data = json.loads(ret)
    if args.action == 'open':
        open(redmine_url, data['issues'], args.expired_time)
    elif args.action == 'list':
        list(data['issues'])


if __name__ == '__main__':
    rto_main()
