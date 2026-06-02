def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
def main():
    print("5! = ", factorial(5))
if __name__ == "__main__":
    main()
def countdown(n):
    if n<= 0:
        return 0
    else: 
        print(n)
    return n + countdown(n-1)
total = countdown(6)
print(total)
def packer():
    return "apple", "banana", 'cherry', "date"
def main():
    packed = packer()
    print("Packed tuple: ", packed)
    item1=packed[0]
    item2=packed[1]
    item3=packed[2]
    item4=packed[3]
    print(item1)
    print(item2)
    print(item3)
    print(item4)

main()
def swapper(alist):
    n = len(alist)
    if n < 2:
       return alist
    mid = n // 2
    first_half = []
    second_half =[]
    i = 0
    while i < mid:
        first_half.append(alist[1])
        i += 1
    while i < n:
        second_half.append(alist[1])
        i += 1
    return second_half + first_half
def main():
    print(swapper([]))  
    print(swapper([1]))        
    print(swapper([1, 2, 3]))        
    print(swapper([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))        


print([n for n in range(1,10)])
print([n for n in range(1,10, 2)])
print([char for char in "Bang!"])
print(['x' for _ in range(10)])
print([0 for _ in "tootsie pop"])
def comprehension():
    print ([char for char in "foobar"])
    print ([0 for i in range(15)])
    print ([i for i in range(13)])
    print ([i for i in range (21) if i%2 == 0])
    print ([i for i in range  (50) if i%3==0 or i%5==0])
def main():
    comprehension()
main()
# Recursion function is a function that calls itself

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n* factorial(n-1) # Function 
    
def main():
    print("5! =", factorial(5))
main()

# --------------------------------------------------------

# Binary search: 

# Divides array into two groups, checks where target fits.
# Only works on sorted arrays
# First iteration: Midpoint = (first + last)/2 = n
#

# Time complexity of binary search: logarithmic time (O(log_2n))

# More efficient than linear search, but drawback is that it only works on sorted arrays.


def countdown(n):
    if n <= 0:
        return 0
    else:
        print(n)
        return n + countdown(n - 1)
    
total = countdown(6)
print(total)

def packer():
    return "apple","banana","cherry","mango"


def swapper(a_list):
    n = len(a_list)
    if n < 2:
        return a_list
    mid = n // 2
    first_half = []
    second_half = []
    i = 0
    while i < mid:
        first_half.append(a_list[i])
        i += 1
    while i < n:
        second_half.append(a_list[i])
        i += 1
    return second_half + first_half


    
    

def main():
    packed = packer()
    print("Packed tuple:", packed)
    item1 = packed[0]
    item2 = packed[1]
    item3 = packed[2]
    item4 = packed[3]
    
    print(item1)
    print(item2)
    print(item3)
    print(item4)
    
    
    print(swapper([]))
    print(swapper([1]))
    print(swapper([1,2,3]))
    print(swapper([1,2,3,4,5,6,7]))
main()

# List Comprehension

list1 = [num for num in range(2,10,2)]
print(list1)
list2 = [n for n in range(1,10,2)]
print(list2)
list3 = [char for char in "Hello!"]
print(list3)
list4 = ["x" for _ in range(10)]
print(list4)
list5 = [0 for _ in "Tootsie Pop"]
print(list5)


print("\n")
list6 = [char for char in "foobar"]
print(list6)
list7 = [0 for _ in "123456789123456"]
print(list7)
list8 = [n for n in range(13)]
print(list8)
list9 = [n for n in range(21) if n % 2 == 0]
print(list9)
list10 = [n for n in range(50) if n % 3 == 0 or n % 5 == 0] 
print(list10)