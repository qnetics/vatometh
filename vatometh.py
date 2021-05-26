#!/bin/env python3
import sys
from src.auto import Automate_run

if __name__ == "__main__" :

    try:

        Automate_run(

            sys.argv[1],

            sys.argv[2],

            sys.argv[3]

        ).FilenameExecute()

    except KeyboardInterrupt:

        print("\nEXIT")