import os
os.system("echo hello terminal command diff  should work")
y=os.popen("diff ")#excute diff  command
y=y.read()
print(y)

