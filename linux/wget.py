import os
os.system("echo hello terminal command wget should work")
y=os.popen("wget")#excute wget command
y=y.read()
print(y)

