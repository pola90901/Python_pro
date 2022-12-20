import os
os.system("echo hello terminal command jed should work")
y=os.popen("jed")#excute jed command
y=y.read()
print(y)

