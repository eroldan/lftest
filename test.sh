#!/bin/bash

ansible all -i inventory -m shell --user vagrant --become -a "$@"
