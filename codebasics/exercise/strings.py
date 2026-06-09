#Address details
street="bazzar street"
city="madanapalli"
country="India"
#create address with + symbol
address1=street+",\n "+city+",\n "+country
address2=f"{street},\n{city},\n {country}"

print(address1)
print(address2)
#this is using for slicing
stmt="Earth revolves around the sun"
print(stmt[6:14])
print(stmt[-3:])
# using f string print how many fruits and vegetables i eat
x=10
y=4
eat=f"I eat {x} vegetables and {y} fruits daily"
print(eat)
eat="I eat {x} vegetables and {y} fruits daily".format(x=x,y=y)
print(eat)

stmt="maine 200 banana khaye"
new_stmt=stmt.replace("banana","samosa")
new_stmt=new_stmt.replace("200","10")
print(new_stmt)
#with single statment
stmt="maine 200 banana khaye"
stmt=stmt.replace("banana","samosa").replace("200","10")
print(stmt)