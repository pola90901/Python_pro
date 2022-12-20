import os
os.system("echo hello terminal command mv should work")
y=os.popen("mv")#excute mv command
y=y.read()
print(y)

