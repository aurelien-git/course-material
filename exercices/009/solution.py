#!/usr/bin python3
# -*- coding: utf-8 -*-

"""
License    : GNU GPL v3 or later
Author     : Aurélien
Mail       : aurelien@hackers.camp
Project    : Number of word in a paragraph
Created on : Tue Sep 30 17:59:30 2014

References
 [split](https://docs.python.org/3/library/stdtypes.html#str.split)
 [list](https://docs.python.org/3/tutorial/introduction.html#lists)
 [len](https://docs.python.org/3/library/functions.html#len)

Course material at
https://github.com/hackinscience/hackinscience.github.io/wiki/Start-Here

"""
phantom_menace = """Turmoil has engulfed the Galactic Republic. The\
 taxation of trade routes to outlying star systems is in\
 dispute. Hoping to resolve the matter with a blockade of deadly\
 battleships, the greedy Trade Federation has stopped all shipping to\
 the small planet of Naboo. While the congress of the Republic\
 endlessly debates this alarming chain of events, the Supreme\
 Chancellor has secretly dispatched two Jedi Knights, the guardians of\
 peace and justice in the galaxy, to settle the conflict"""

words = phantom_menace.split(" ")

print(len(words))
