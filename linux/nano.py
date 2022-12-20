import os
os.system("echo hello terminal command nano should work")
y=os.popen("nano")#excute nano command
y=y.read()
print(y)

