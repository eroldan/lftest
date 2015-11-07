#!/bin/bash

ansible-playbook -i inventory --user vagrant prepare.yml "$@"
