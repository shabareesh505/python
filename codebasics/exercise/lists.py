import math

from codebasics.exercise.numbers import length

#expences for every month will be stored in lists
month=["January","February","March","April","May"]
expenses=[2200,2350,2600,2130,2190]
#in feb how may dolors more you spent when compared to january
if expenses[month.index("January")]<expenses[month.index("February")]:
    print("in Feb i have spent",expenses[month.index("February")]-expenses[month.index("January")],"dollars than jan")
#find total expenses of first quarter
print("the total expenses in first quarter is",expenses[month.index("January")]+expenses[month.index("February")]+expenses[month.index("March")])
if 2000 in expenses:
    print("yes i have spent exact 2000 dollars in",month[expenses.index("2000")])
else:
    print("no i have spent exact 2000 dollars in any month")
# add your expense on June to you list
month.append("june")
expenses.append(1980)
print(expenses)
#return amount for the month of April to be adjusted
expenses[month.index("April")]+=200
print("expense amount of April after adjestment",expenses[month.index("April")])
# second exercise
heros=['spider man','thor','hulk','iron man','captain america']
print("the length on the list", len(heros))
heros.append('black panther')
print(heros)
heros.remove("black panther")
heros.insert(heros.index("hulk")+1,"black panther")
heros[1:3]=["doctor strange"]
#heros[1]="test"
print(heros.sort())
print(heros)

