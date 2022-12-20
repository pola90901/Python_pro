import os
os.system("echo hello terminal command man should work")
y=os.popen("man")#excute man command
y=y.read()
print(y)

