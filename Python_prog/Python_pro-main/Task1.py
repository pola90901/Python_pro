# Application for simple calculator using python lang with 2 modes scientific and programming
#asking the user to enter two values to do the math 


print("**********************Welcome to calculator programme**************************")
print("please select your mode")
print("for scientific calculator press: 1 , for programming calculator press 2")
mode=int(input(" your choice : " ))


if mode == 1:							##### scientific calculator
	print("welcome to scientific calculator ") 
	print("(Hint input numbers cant be a string)  	 ")
	op1=float(input("please enter number 1:"))
	op2=float(input("please enter number 2:"))
	operator=input("please select the operator '+ , - '*' '/', '%' ,'**' ,'//' :  ")
	if operator == '+':						#addition
		print("you select addition")
		print(op1+op2)	
	elif operator == '-':	
		print("you select subtraction num1 - num2")
		print(op1-op2)
	elif operator == '*':					#subtraction
		print("you select multiplication")
		print(op1*op2)
	elif operator == '/':					#division wit making sure that the dimenator is not equal zero
		print("you select division  num1 /num2")
		if op2 != 0:
			print(op1/op2)
		else :
			print("second number can't be = zero")
	elif operator == '%':					# moduls	
		print("you select modules  num1 % num2 ")
		print(op1%op2)		
	elif operator == "**":					#exp
		print("you select exp  num1 ** num2 ")
		print(op1**op2)						
	elif operator == "//":					#floor division
		print("you select floor division  num1 // num2 ")
		print(op1//op2)
	else :
		print(" wrong input operator")
elif mode == 2:							##### programming calculator
	print("welcome to scientific calculator ")
	print("Hint input numbers cant be a float nor a string :) ")
	op_1=int(input("please enter number 1:"))
	op_2=int(input("please enter number 2:"))
	operator_1=input("please select the operator '+ , - '*' '/', '%' ,'**' ,'//' :  ")
	rep=input("you want the result in BIN or HEX or DEC or OCT  please enter the choice as string : ")
	if operator_1 == '+':						#addition
		print("you select addition")
		if rep == "BIN":
			print(bin(op_1+op_2))
		elif rep == "HEX":
			print(hex(op_1+op_2))
		elif rep == "DEC":
			print(op_1+op_2)
		elif rep == "OCT":
			print(oct(op_1+op_2))
		else:
			print("wrong input string please choose between the BIN or HEX or DEC or OCT capitalized ")
	elif operator_1 == '-':						#subtraction
		print("you select subtraction num1 - num2 ")
		if rep == "BIN":
			print(bin(op_1-op_2))
		elif rep == "HEX":
			print(hex(op_1-op_2))
		elif rep == "DEC":
			print(op_1-op_2)
		elif rep == "OCT":
			print(oct(op_1-op_2))
		else:
			print("wrong input string please choose between the BIN or HEX or DEC or OCT capitalized ")

	elif operator_1 == '*':					#multiplication
		print("you select multiplication")
		if rep == "BIN":
			print(bin(op_1*op_2))
		elif rep == "HEX":
			print(hex(op_1*op_2))
		elif rep == "DEC":
			print(op_1*op_2)
		elif rep == "OCT":
			print(oct(op_1*op_2))
		else:
			print("wrong input string please choose between the BIN or HEX or DEC or OCT capitalized ")		
	elif operator_1 == '/':					#division with making sure that the dimenator is not equal zero
		print("you select division  num1 /num2")
		if op2 != 0:
			if rep == "BIN":
				print(bin(op_1*op_2))
			elif rep == "HEX":
				print(hex(op_1*op_2))
			elif rep == "DEC":
				print(op_1*op_2)
			elif rep == "OCT":
				print(oct(op_1*op_2))
			else:
				print("wrong input string please choose between the BIN or HEX or DEC or OCT capitalized ")		
				print(op_1/op_2)
		else :
			print("second number can't be = zero")
	elif operator_1 == '%':					# moduls	
			print("you select modules  num1 % num2 ")
			if rep == "BIN":
				print(bin(op_1%op_2))
			elif rep == "HEX":
				print(hex(op_1%op_2))
			elif rep == "DEC":
				print(op_1%op_2)
			elif rep == "OCT":
				print(oct(op_1%op_2))
			else:
				print("wrong input string please choose between the BIN or HEX or DEC or OCT capitalized ")		
						
	elif operator_1 == "**":					#exp
		print("you select exp  num1 ** num2 ")
		if rep == "BIN":
			print(bin(op_1**op_2))
		elif rep == "HEX":
			print(hex(op_1**op_2))
		elif rep == "DEC":
			print(op_1**op_2)
		elif rep == "OCT":
			print(oct(op_1**op_2))
		else:
			print("wrong input string please choose between the BIN or HEX or DEC or OCT capitalized ")		
								
	elif operator_1 == "//":					#floor division
		print("you select floor division  num1 // num2 ")
		if rep == "BIN":
			print(bin(op_1**op_2))
		elif rep == "HEX":
			print(hex(op_1**op_2))
		elif rep == "DEC":
			print(op_1**op_2)
		elif rep == "OCT":
			print(oct(op_1**op_2))
		else:
			print("wrong input string please choose between the BIN or HEX or DEC or OCT capitalized ")	

	else :
		print(" wrong input operator")
else :	#invalid choice
	print("invalid choice")	

