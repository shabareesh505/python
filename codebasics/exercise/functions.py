def calculate_area(base,height):
    return (1/2)*(base*height)
def calculate_area(base,height,choice):
    if choice=="Triangle":
        return (1/2)*(base*height)
    elif choice=="Rectangle":
        return base*height
    else:
        return (1/2)*(base*height)
def pattern(value):
    for i in range(1, value+1):
        for j in range(1, value+1):
            if i >= j:
                print("*", end="")
        print()
if __name__=="__main__":
 #   base=int(input("enter the base of triangle"))
 #   height=int(input("enter the height of triangle"))
 #   area=calculate_area(4,5)
  #  print("area of triangle is ",area)
    area=calculate_area(4,5,"Triangle")
    print("area of triangle is ",area)
    area=calculate_area(4,5,"Rectangle")
    print("area of Rectangle is ",area)
    pattern(int(input("enter your number to print pattern")))

