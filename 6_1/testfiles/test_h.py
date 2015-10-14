BEGIN COPYRIGHT
END COPYRIGHT


import getopt, sys, os, re

""" ------------------------------------------------------------------------------------------------------------------------------------ """

def load_file(filename): 
    temp = ''
    with open(filename) as file:
        for line in file: 
            temp += line
    return temp



