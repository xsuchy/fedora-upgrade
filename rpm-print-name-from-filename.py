#!/usr/bin/python3
import dnf
import sys

subject = dnf.subject.Subject(sys.argv[1])
possible_nevra = subject.get_nevra_possibilities()
print(possible_nevra[0].name)

