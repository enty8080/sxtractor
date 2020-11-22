#!/usr/bin/env python3

import sys
import re

class sxtractor:
    def help_usage():
        print("Usage: objdump -d <input_file> | sxtractor")

    def sxtract():
        shellcode = ""
        lenght = 0
        if not sys.stdin.isatty():
            try:
                while 1:
                    item = sys.stdin.readline()
                    if item:
                        if re.match("^[ ]*[0-9a-f]*:.*$",item):
                            item = item.split(":")[1].lstrip()
                            x = item.split("\t")
                            opcode = re.findall("[0-9a-f][0-9a-f]",x[0])
                            for i in opcode:
                                shellcode += "\\x" + i
                                lenght += 1
                    else: 
                        break
            except:
                help_usage()
            print(shellcode)
            print("Shellcode Lenght: " + str(lenght))
        else:
            help_usage()
