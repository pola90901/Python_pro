import os
os.system("echo hello terminal command du  should work")
y=os.popen("du ")#excute du  command
y=y.read()
print(y)

