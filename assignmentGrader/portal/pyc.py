	
def go():
    import subprocess

    if subprocess.call(["gcc", "hello.c"]) == 0:
        subprocess.call(["./a.out <input.txt >output.txt"], shell=True)
        print "Compiled Successfully"
    else: print "Compilation errors"