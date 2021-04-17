#!/usr/bin/python3

import os
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter


BashCompleter = WordCompleter(['echo', 'ls', 'cat'], ignore_case=True)



while 1:
    inp = prompt(u'> ', history=FileHistory('.jamshell_history'), auto_suggest=AutoSuggestFromHistory(), completer=BashCompleter)
    if inp == "quit" or inp == "exit":
        break
    try:
        os.system(inp)
    except:
        print("Invalid Command")














