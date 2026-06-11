india = ["mumbai", "bangalore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city=input("enter city which you are belongs to")

if city in india:
    print("You are belongs to India")
elif city in pakistan:
    print("You are belongs to Pakistan")
elif city in bangladesh:
    print("You are belongs to Bangladesh")
else:
    print("You are not belongs to India, Pakistan, Bangladesh")

city=input("enter first city")
city2=input("enter second city")
if city in india and city2 in india:
    print("those cities are belongs to India")
elif city in pakistan and city2 in pakistan:
    print("those cities are belongs to Pakistan")
elif city in bangladesh and city2 in bangladesh:
    print("those cities are belongs to Bangladesh")
else:
    print("those cities are not belongs to same county")

sugar=int(input("enter fasting sugar leval"))

if sugar < 80:
    print("your blood sugar leval is low")
elif sugar > 100:
    print("your blood sugar leval is high")
else:
    print("your blood sugar leval is normal")
