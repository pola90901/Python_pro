import os
os.system("echo hello terminal command htop should work")
y=os.popen("htop")#excute htop command
y=y.read()
print(y)

