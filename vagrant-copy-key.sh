#!/bin/bash
#
# Script to upload your ssh pub key to all running Vagrant machines


for machine in $(vagrant status | grep -e '.*\srunning.*' | cut -d ' ' -f 1)
do
    echo $machine
    cat ~/.ssh/id_rsa.pub | vagrant ssh $machine --command "cat >> ~/.ssh/authorized_keys"
done

