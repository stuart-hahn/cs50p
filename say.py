import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("I'm hungry, " + sys.argv[1])
