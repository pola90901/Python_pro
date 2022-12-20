import os
os.system("echo hello terminal command rmdir  should work")
y=os.popen("rmdir ")#excute rmdir  command
y=y.read()
print(y)

