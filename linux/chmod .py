import os
os.system("echo hello terminal command chmod  should work")
y=os.popen("chmod ")#excute chmod  command
y=y.read()
print(y)

