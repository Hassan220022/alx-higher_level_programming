#!/usr/bin/python3
import codecs
def read_file(filename=""):
    with codecs.open(filename, 'r', encoding='utf-8') as f:
        return f.read()    