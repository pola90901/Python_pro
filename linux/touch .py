import os
os.system("echo hello terminal command touch should work")
y=os.popen("touch")#excute touch command
y=y.read()
print(y)

