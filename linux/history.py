import os
os.system("echo hello terminal command history should work")
y=os.popen("history")#excute history command
y=y.read()
print(y)

