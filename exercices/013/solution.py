#!/usr/bin python3
# -*- coding: utf-8 -*-

"""
License    : GNU GPL v3 or later
Author     : Aurélien DESBRIERES
Mail       : aurelien@hackers.camp
Project    : Script that print the first parameter given to the script
Created on : Wed Oct  1 10:13:44 2014

References

Maybe you will need to import few modules in your program.

 [argv](https://docs.python.org/3.4/library/sys.html)
 [sys.argv] https://docs.python.org/3/library/sys.html#sys.argv
 [import](https://docs.python.org/3/reference/simple_stmts.html#import)
 [if](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
 [len](https://docs.python.org/3/library/functions.html#len)

Course material at
https://github.com/hackinscience/hackinscience.github.io/wiki/Start-Here

"""

import sys

if len(sys.argv) > 1:
    print(sys.argv[1])
