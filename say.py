#import cowsay
import sys
"""
if len(sys.argv) == 2:
    cowsay.cow("Hello, "+ sys.argv[1])
if len(sys.argv) == 2:
    cowsay.trex("Hello, "+ sys.argv[1])"""
from sayings import hello
if len(sys.argv) ==2:
    hello(sys.argv[1])

