import sys
import os
import json
import requests

def create():
    repoName = str(sys.argv[1])
    headers = {'Authorization': 'token f8eb9975b3ebee91b42eb3b052d0158455ec1867'}
    req = requests.post('https://api.github.com/user/repos', headers=headers, json={'name': repoName})
   
    if('name' in req.json().keys()):
        print("Starting...")
    else:
        print("Fail")
    sys.exit(0)


if __name__ == '__main__':
    create()
