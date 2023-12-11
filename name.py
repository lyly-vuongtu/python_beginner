import sys
"""
try:
# python name.py Lyly
    print("hello, my name is",sys.argv[1])
except IndexError:
    print("Too few arguments")"""

# check for errors
if len(sys.argv)<2:
    sys.exit("Too few arguments")
#elif len(sys.argv) > 2:
#    sys.exit("Too many arguments")
# print name tags
#print("hello, my name is",sys.argv[1])
for arg in sys.argv[1:]:
    print("hello, my name is",arg)
