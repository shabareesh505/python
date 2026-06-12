result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count=0
for i in result:
    if i=="heads":
        count+=1
print("the count of heads is",count)

print("the squires of odd numbers between 1 to 10")
for i in range(1,11):
    if i%2!=0:
        print(i**2)
expense_list = [2340, 2500, 2100, 3100, 2980]
month=["January","February","March","April","May"]
expense=int(input("enter your expense"))
if expense in expense_list:
    print("your expense is belongs to ",month[expense_list.index(expense)])
else:
    print("your expense is not in the list")
#you are in race i will ask are you ok for every 1 km
err=0
for i in range(1,6):
    if input("are you tired?")=="yes":
        err=1
        break
if err==1:
    print("you didn't finish the race")
else:
    print("you have finished the race")

for i in range(1,6):
    for j in range(1,6):
        if i>=j:
            print("*",end="")
    print()
