import os
os.system("echo hello terminal command find  should work")
y=os.popen("find ")#excute find  command
y=y.read()
print(y)

