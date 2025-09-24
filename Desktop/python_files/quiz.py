
def even_odd(number): # function to check even or odd
    if number % 2 == 0:
        return "Even Number"
    else:
        number % 2 != 0
        return "Odd Number"
def positive_negative(number):    #function to check if it's postive or negative
    if number > 0:
        return "Positive Number"
    else:
        return "Negative Number"
def square(number):  #function to find square of the number
    return number * number    
def cube(number):
      #function to find cube of the number
    return number * number * number
def main():
   """Main function to call on all other functions"""
number = int(input("Enter a Number: "))
print(even_odd(number))
print(positive_negative(number))
print("Square of this Number is:", square(number))
print("Cube of this Number is: ", cube(number))
main()
   