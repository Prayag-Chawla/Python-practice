import random

def passwordgen(length):
	symbolseq=["$","#","%","_","~"]
	name = input("Ur name here \n")
	color = input("Ur favorite color \n").upper()
	randomnumber = random.randint(1,100)
	symbols_1 = random.choice(symbolseq)
	symbols_2 = random.choice(symbolseq)
	subject = input("Favorite subject \n")
	if(length>8):
		print(name+symbols_1+symbols_2+color+subject+str(randomnumber))
	if(length<8):
		print(name+symbols_1+symbols_2+color+str(randomnumber))
	else: 
		print(name+symbols_1+symbols_2+color+str(randomnumber))
		
		
		
		
passwordgen(8)

