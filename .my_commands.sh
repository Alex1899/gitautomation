#!/bin/bash

function create(){
    result=`python3 ~/my_commands/create.py $1`
    echo "$result"
    if [ "$result" == "Starting..." ]; then
        cd ~/Projects && mkdir $1
        cd $1
        git init
        git remote add origin git@github.com:Alex1899/$1.git
        touch README.md 
        git add .
        git commit -m 'first commit'
        git push -u origin master 
        echo "Repo $1 created successfully :)"
        code .
    else
        echo 'There was an error when creating the repo :('
    fi
   
}