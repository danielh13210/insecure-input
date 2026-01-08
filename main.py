#!/usr/bin/env python2

import random

def randbit():
  return int(round(random.random()))
def randbits(b):
  c=0
  for i in range(b):
    c=(c<<1)+randbit()
  return c

token = randbits(16)

input("Enter your name: ")
if int(raw_input("secret: "))==token:
  print "success!"
else:
  print "fail! try again."
