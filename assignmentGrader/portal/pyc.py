	
import subprocess

if subprocess.call(["gcc", "add.c"]) == 0:
    subprocess.call(["./a.out <input.txt >output.txt"], shell=True)
else: print "Compilation errors"