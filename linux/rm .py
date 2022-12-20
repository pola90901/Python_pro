import os
os.system("echo hello terminal command rm  should work")
y=os.popen("rm ")#excute rm  command
y=y.read()
print(y)

