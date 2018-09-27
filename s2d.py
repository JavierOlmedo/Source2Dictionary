#!/usr/bin/python3

#IMPORTS
from s2d.main import main
from lib.output import error

#MAIN
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        error("[-] User aborter session")