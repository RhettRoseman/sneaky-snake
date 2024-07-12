
import cowsay
import sys

if len(sys.argv) > 1:
    cowsay.trex('hello, ' + sys.argv[1])
    