import random
fname = input("Enter your frist name: ")
lname = input("Enter your last name: ")
year = input("Enter your birth year: ")

dic = {"fname":fname,"lname":lname,"year":year}

n_list = list(dic.values())

for i in range(3):
  random.shuffle(n_list)
  r = ''.join(n_list)
  print(r+"@gmail.com")