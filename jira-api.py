#! /usr/bin/env python3
import requests
from requests import Session
import json
from pprint import pprint as pp
from getTokenAWS import parameter_store as ps
# docs https://developer.atlassian.com/cloud/jira/platform/rest/v2/intro

class jiraCall:
   def __init__(self,token):
        self.apiurl = 'https://somecompany.atlassian.net/rest/api/2/' 
        self.headers = {
            "Content-type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
            "Authorization": "Basic " + token,
        }
        self.session = Session()
        self.session.headers.update(self.headers)

   def getIssues(self):
       url = self.apiurl + 'issue/SPIKE-1023'
       r = self.session.get(url, headers=self.headers)
       data = (json.dumps(json.loads(r.text), sort_keys=True, indent=4, separators=(",",": ")))
       return data

   def getPermissions(self):
       url = self.apiurl + 'mypermissions?'
       query = {
       'permissions': 'BROWSE_PROJECTS,EDIT_ISSUES'
       }
       r = self.session.get(url, headers=self.headers, params=query)
       data = (json.dumps(json.loads(r.text), sort_keys=True, indent=4, separators=(",",": ")))
       return data
    
   def getMyself(self):
       url = self.apiurl + 'myself?expand=applicationRoles,groups'
       r = self.session.get(url, headers=self.headers)
       data = (json.dumps(json.loads(r.text), sort_keys=True, indent=4, separators=(",",": ")))
       return data

def main():
    j = jiraCall(ps('jira_auth_api_token'))
    issues = j.getIssues()
    perm = j.getPermissions()
    myself = j.getMyself()
    #pp(issues)
    pp(myself)
    #pp(perm)

if __name__ == '__main__':
    main()
