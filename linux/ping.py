import os
os.system("echo hello terminal command ping should work")
y=os.popen("ping")#excute ping command
y=y.read()
print(y)

