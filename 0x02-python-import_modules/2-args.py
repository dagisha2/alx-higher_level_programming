#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = len(sys.argv[1:])
    if args != 1:
        if args == 0:
            print("{} arguments.".format(0))
        else:
            print("{} arguments:".format(args))
            i = 1
            i <= args
            for argv in sys.argv:
                if argv[0:2] != "./":
                    print("{}: {}".format(i, argv))
                    i += 1
    else:
        print("{} argument:".format(1))
        for argv in sys.argv:
            if argv[0:2] != "./":
                print("{} {}".format(1, argv))
