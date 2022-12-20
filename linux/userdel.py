import os
os.system("echo hello terminal command userdel should work")
y=os.popen("userdel")#excute userdel command
y=y.read()
print(y)

