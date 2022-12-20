import os
os.system("echo hello terminal command tail  should work")
y=os.popen("tail ")#excute tail  command
y=y.read()
print(y)

