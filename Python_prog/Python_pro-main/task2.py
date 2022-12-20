## drawing rotating arrow
import os
from time import sleep

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

while 1:
	i=1
	w=1
	''' 
       *
       * *
       * * *
       * * * *
       * * * * *
 * * * * * * * * *
       * * * * *
       * * * *
       * * *
       * *
       *
	'''
	for x in range(0, 6):
		if x != 5:print("      ",end="")
		else:print(" * * *",end="")
		for y in range(0,x+1):
			print(" *",end="")
		print("")	
			
	for x in range(6,0,-1 ):
		print("      ",end="")
		for y in range(1,x):
			print(" *",end="")
		print("")
	sleep(2)   
	#print("", flush=True)
	cls()	
	##################################     |
				''' 
		   *
           *
           *
 * * * * * * * * * * *
   * * * * * * * * *
     * * * * * * *
       * * * * *
         * * *
           *		
				'''				
	for x in range(0, 4):
		if x!=3:
			print("           *")
		else :
			for y in range(0,11):
				print(" *",end="")
			print("")	
			for y in range (9,0,-2):
				print("  "*i,end="")
				i+=1
				print(" *"*(y))
	################################
	'''   
		   *
         * *
       * * *
     * * * *
   * * * * *
 * * * * * * * * *
   * * * * *
     * * * *
       * * *
         * *
           *

		   '''
	sleep(2)
	cls()	
	
	for x in range(11, 1,-2):
		print(" "*(x-1),end="")
		print(" *"*w)
		w+=1
	z=1
	for y in range(0,9):
		print(" *",end="")
	print("")	
	for x in range(5, 0,-1):
		print("  "*z,end="")
		print(" *"*(x),end="")
		print()
		z+=1
	###########################	
	'''   
		   *
         * * *
       * * * * *
     * * * * * * *
   * * * * * * * * *
 * * * * * * * * * * *
           *
           *
           *
		   
		   '''
	sleep(2)   
	cls()	

	z = 5
	x = 1
	for i in range(6):
		print('  ' * z + ' *' * x + '  ' * z)
		x+=2
		z-=1	
	for i in range(3):
			print(" "*11+"*")
	sleep(2)   
	cls()

		
