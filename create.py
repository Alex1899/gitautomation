import sys
import os
import json
import requests

def create():
    repoName = str(sys.argv[1])
    headers = {'Authorization': 'token 813e9fd5378b8307102c5709d850e7b68f24c217'}
    req = requests.post('https://api.github.com/user/repos', headers=headers, json={'name': repoName})
   
    if('name' in req.json().keys()):
        print("Starting...")
    else:
        print("Fail")
        print(req.json())
    sys.exit(0)


if __name__ == '__main__':
    create()
