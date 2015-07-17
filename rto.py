#!/usr/bin/env python

import urllib2
import json
import os

def main():
    redmine_url = os.environ['REDMINE_URL']
    api_key = os.environ['REDMINE_API_KEY']
    rest_url = redmine_url + 'issues.json?key=' + api_key + '&status_id=open&assigned_to_id=me'
    req = urllib2.Request(rest_url)
    try:
        res = urllib2.urlopen(req)
        ret = res.read()
        data = json.loads(ret)
        for issue in data['issues']:
            issue_url = redmine_url + "issues/" + str(issue['id'])
            os.system('open ' + issue_url)

    except urllib2.HTTPError:
        print "error"


if __name__ == '__main__':
    main()
