import os
os.system("echo hello terminal command grep  should work")
y=os.popen("grep ")#excute grep  command
y=y.read()
print(y)

