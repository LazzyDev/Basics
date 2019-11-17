
import time

max_weight = 500
pass_list = {}
total_weight = 0

while(total_weight < max_weight):
	names = input("enter name: ")
	pass_weight = int(input("enter weight: "))

	total_weight += pass_weight
	
	if(pass_weight > max_weight):
		print("overweight")
		break
	else:
		for i in range(max_weight):
			pass_list[names]=pass_weight

else:
	print("lift is Full")
	print(pass_list)
		

