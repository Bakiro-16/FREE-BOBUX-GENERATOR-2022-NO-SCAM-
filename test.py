#This is a test doc I used to test some stuff I had trouble with


from time import sleep
import sys


def print_slowly(text):
    for c in text:
        print(c, end='')
        sys.stdout.flush()
        sleep(0.5)

print_slowly('................')