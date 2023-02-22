#!/usr/bin/python3
import re

write_to = "gdbinit"
with open(f'{write_to}', 'w') as f:
    args = gdb.execute("show args", True, True)
# Substrings are used for "show args" as GDB returned values should be syntactically consistent
    args = args[68:-3]
# for "info file", we will use substrings and regex as the entry point and section info might vary
    file_info = gdb.execute("info file", True, True)
    file_name = re.search(r"Symbols.*\"\.", file_info)
    file_name = file_name.group(0)[14:-2]
    file_type = re.search(r"\, file type .*", file_info)
    file_type = file_type.group(0)[2:-1]
    print(f'(っ◕‿◕)っ')
    print(f"Writing to '{write_to}'")
    print(f"Current executable: {file_type}")
# demarcate as gdb-script mode for emacs
    f.write("# -*- mode: gdb-script; -*-\n")
# good idea to set as sometimes the command arguments have chars that the shell tries to interpret
    f.write("set startup-with-shell off\n")
    f.write(f"# {file_type}\n")
    f.write(f"file {file_name}\n\n")
    f.write(f"set args {args}\n")

# This is optional. Use when stopping at cc1 suffices
usr_choice = input("Continue to next executable? (Case insensitive 'y' or 'yes'. Anything else quits.)")
usr_choice = usr_choice.lower()
if usr_choice == 'y' or usr_choice == "yes":
    gdb.execute("quit")
gdb.execute("quit 1")
