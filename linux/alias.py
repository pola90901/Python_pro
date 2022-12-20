import os
os.system("echo hello terminal command alias should work")
y=os.popen("alias")#excute alias command
y=y.read()
print(y)

