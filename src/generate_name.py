#!/usr/bin/env python2.7
import names

def gen_names(num):
    allnames = []
    for i in range(num):
        allnames.append(str(names.get_full_name())+str(i))

    return allnames

if __name__ == "__main__":
    allnames = gen_names(100)
    print allnames
