import os
os.system("echo hello terminal command zip should work")
y=os.popen("zip")#excute zip command
y=y.read()
print(y)

