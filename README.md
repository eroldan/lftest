# Story

* https://www.toptal.com/uploads/note/attachment/181548/Linux_Foundation_-_Linux_Systems_Programmer.html

# Dependencies

```
pip install shell.py
pip install ansible
```

# Setup test environment

```
vagrant up
./vagrant-copy-key.sh # install *your* ssh public key to the vagrant vms
./prepare.sh # this runs ansible and install few deps on test systems
```

# Test items
Check example.log

