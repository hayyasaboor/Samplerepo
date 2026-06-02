try:
    x= int(input("Enter x: "))
    y= int(input("Enter y: "))

    print("x/y= ", x/y)
except ValueError:
    print("invalid number entered")
except ArithmeticError:
    print("cant divide by 0")    
      