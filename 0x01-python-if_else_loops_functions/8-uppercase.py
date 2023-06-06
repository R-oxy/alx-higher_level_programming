#!/usr/bin/python3
def uppercase(str):
  for ch in str:
    if ch.islower():
      ch = ch.upper()
    print(ch, end="")
  print()
