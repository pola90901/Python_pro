import os
os.system("echo hello terminal command useradd should work")
y=os.popen("useradd")#excute touch command
y=y.read()
print(y)

