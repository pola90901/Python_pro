import os
os.system("echo hello terminal command uname should work")
y=os.popen("uname")#excute uname command
y=y.read()
print(y)

