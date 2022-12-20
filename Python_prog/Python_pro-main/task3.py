my_shop={"products":[["apples",20,"Cost in $ =",2],["bannaa",30,"Cost in $ =",3],["cherry",50,"Cost in $ =",4]]}
while(1):
	print("               welcome to ITI shop")
	print("1- customr")
	print("2- owner")
	print("3- exit")
	choice=int(input("Select Mode For customer press 1 , for owner press 2 , to exist press 0 :"))
	if choice ==1:
		print("Welcome Customr")
		print("- To show our products       press 1")
		print("- To Buy from our products   press 2")
		print("-to exit                     press 0")
		op1=int(input(" your choice: "))
		if op1==1:
			print(my_shop)
		elif op1==2:
			sum=0
			print(my_shop)
			buy_list=input("please number of product you wish to buy seperatd by space :").split(" ")
			j=0
			for i in buy_list:									# looping of the input values to check 
				val=int(my_shop["products"][j][1])				#casting the value of the stock in the dict to variable name val										
				if int(i) > int(my_shop["products"][j][1]):		#asking if the value enter by the customer is more than the stock 
					print(" your request is beyond our stock for value "+str(i))
				else:
					val=val-(int(i))							#reduce the stock of the shop by the values enter by customer
					my_shop["products"][j][1]=val				#putting the new stock in the shop
					price=int(my_shop["products"][j][3])		#getting the price of the desired product
					sum=sum+(price)*(int(i))					#calculating the sum to calculate the bill (product price * required amount)
					j+=1										#iterator to iterat on the index of the list name buy_list



					
			print("you bill total value ="+str(sum)+"$")		#showing th bill
			print(my_shop)
		elif op1==0:
			print("thank you")
		else:
			print("invalid choice")
	elif choice ==2:
		print("Welcome owner")
		print("-to Add new products         press 1")
		print("- To Show Products           press 2")
		print("- to Change cost             press 3")
		print("- to delete product          press 4")	
		print("-to exit                     press 0")
		op2=int(input(" your choice :"))
		if op2==1:
			print("please be careful when entering product details")
			add=input("please enter the product name ,stock , Cost in $ = , cost Seperated by space :").split(" ")
			my_shop["products"].append(add)	
		elif op2==2:
			print(my_shop)
		elif op2==3:
			name_of_product=input("please enter the name of the product to change its price :")		
			for i in my_shop["products"]:					#looping on the dict with every once i is equal to list
				if name_of_product == i[0]:					# asking if the input by customer is equal the name in the list in dict or no	
					new_cost=input("please enter new cost :")
					i[3]=new_cost							#putting the new cost on the same list
				else:
					print("product name not found")
					break;
		elif op2==4:
			prod=input("please enter product name to delete :")
			removed=0										#flag	
			for i in my_shop["products"]:					#looping on the dict with every once i is equal to list
				if prod == i[0]:							#checking if list fist element is equal to the input name from the user 	
					my_shop["products"].remove(i)			#deleting the entire list from the dict name my_shop
					removed=1								#setting flag to 1
					break;		
			if removed ==0:					
				print("product name not found")
			else:	
				print("removed succefully")	
		elif op2==0:
			print("thank you !")		
		else:
			print("invalid choice")			
	elif choice ==0:	
		print("thank you ")
	else :
		print("invalid choice")