import os
os.system("echo hello terminal command tar  should work")
y=os.popen("tar ")#excute tar  command
y=y.read()
print(y)

