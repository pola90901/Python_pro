import os
os.system("echo hello terminal command locate  should work")
y=os.popen("locate ")#excute locate  command
y=y.read()
print(y)

