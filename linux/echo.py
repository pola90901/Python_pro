import os
os.system("echo hello terminal command echo should work")
y=os.popen("echo")#excute echo command
y=y.read()
print(y)

