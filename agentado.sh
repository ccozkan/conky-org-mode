#!/bin/bash

cd /home/cc/Aux/agentado

emacs -batch -l ~/.emacs.d/init.el --eval "(run-hooks 'emacs-startup-hook)" --eval '(org-batch-agenda "t")' 2> /dev/null > /home/cc/Aux/agentado/todos.txt
emacs -batch -l ~/.emacs.d/init.el --eval "(run-hooks 'emacs-startup-hook)" --eval '(org-batch-agenda "a")' 2> /dev/null > /home/cc/Aux/agentado/agenda.txt 

sed -i '/now/ d' agenda.txt
sed -i '/---/ d' agenda.txt

sed -i 1,8d todos.txt

/usr/bin/python3 formatter.py
