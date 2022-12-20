import os
os.system("echo hello terminal command  jobs should work")
y=os.popen("jobs")#excute  jobs command
y=y.read()
print(y)

