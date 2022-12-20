import os
os.system("echo hello terminal command sudo should work")
y=os.popen("sudo")#excute sudo command
y=y.read()
print(y)

