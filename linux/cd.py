import os
os.system("echo hello terminal command cd should work")
y=os.popen("cd")#excute cd command
y=y.read()
print(y)

