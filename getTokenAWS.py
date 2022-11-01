#! /usr/bin/env python3

import boto3

'''
 Beginning of Functions
'''

#Get the bearer token as a secret from aws parameter store 
def parameter_store(bearer):
    ssm = boto3.client('ssm')
    response = ssm.get_parameter(Name=bearer, WithDecryption=True)
    bearer_token = response['Parameter']['Value']
    return bearer_token

def main():
    parameter_store('jira_auth_api_token')
    

if __name__ == '__main__':
    main()
