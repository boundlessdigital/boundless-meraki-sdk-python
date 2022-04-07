#!/bin/bash


git checkout -b meraki-master master
git pull https://github.com/meraki/dashboard-api-python.git master
rm -rf meraki
git add .
git commit -m 'Making space for upstream'
git checkout master
git merge meraki-master
git branch -D meraki-master
