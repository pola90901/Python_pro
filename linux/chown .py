import os
os.system("echo hello terminal command chown  should work")
y=os.popen("chown ")#excute chown  command
y=y.read()
print(y)

