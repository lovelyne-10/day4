# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split()# split the name into list
number_names=len(names)
import random
random_name=random.randint(0,number_names-1)
print(names[random_name])
print(names[random_name]+"he will have to pay for everybody's food bill")

  
  






