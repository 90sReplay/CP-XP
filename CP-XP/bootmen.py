import os
print("Type the location of the file you wan't to boot from.")
print("")
bootfile = input("")
if os.path.exists(bootfile):
    os.system(bootfile)
else:
    print("?Syntax  Error")
    bootfile = input("")
