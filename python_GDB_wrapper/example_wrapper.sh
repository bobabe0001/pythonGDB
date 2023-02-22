#/!bin/bash

~/Dev/builds/DebugMe/bin/gcc main.c -wrapper gdb,-x,setup.py,--args
