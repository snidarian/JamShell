#!/usr/bin/python3


from prompt_toolkit import prompt
from prompt_toolkit import FileHistory


while 1:
    inp = prompt(u'> ', history=FileHistory('history.txt'))
    print(inp)














