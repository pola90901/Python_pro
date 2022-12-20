import os
os.system("echo hello terminal command CAt should work")
y=os.popen("cat")#excute cAT command
y=y.read()
print(y)

