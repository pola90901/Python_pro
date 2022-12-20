import os
os.system("echo hello terminal command df  should work")
y=os.popen("df ")#excute df  command
y=y.read()
print(y)

