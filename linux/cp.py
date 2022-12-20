import os
os.system("echo hello terminal command cp should work")
y=os.popen("cp")#excute cp command
y=y.read()
print(y)

