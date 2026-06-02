'''
seta = {"apple", "banana", "mango", "mango"}
setb = {2, 5, 7}
setc = {1.5, 6.5, 7.5}
setd = {'w', 'e'}
print (setb)
print(len(seta))
print(type(setc))

seta.add("orange")
print(seta)
x ={"apple", "banana", "charry"} 
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
x = {"a", "b", "c"}
y = {"f","e", "d", "c", "b", "a"}
z = y.issuperset(x)
print(z)

def subset(a_set, b_set):
    return a_set.union(b_set)
def main():
    set1 = {1, 2, 3, 4, 5}
    set2 = {2, 3}

    result = subset(set1, set2)
    print("Is set1 a superset of set2?", result)

if __name__ == "__main__":
    main()

def set():
    set1 = {111, 3, 56, 57}
    print("Orginal Set: ", set1)
    set1.add (34)
    set1.add (45)
    set1.add (57)
    print("Set after adding: ", set1)
def main():
    set()
if __name__ == "__main__":
    main()   
def sets():
    set1 = {111, 3, 56, 57}
    set1.add (34)
    set1.add (45)
    set1.add (57)
    string_set = set(("mississippi"))
    print("Set: ", string_set)
def main():
    sets()
if __name__ == "__main__":
    main()

lista = [ 'tea', 'coffee', 'juice']
listc = [5, 2, 3]
listx = ['y', 'r', 't']
listy = {5.5, 4.7, 2.2}
listb = sorted(listy)
print(listb)
print(sorted(lista))
print(sorted(listc))
print(sorted(listx))

lista.sort()
print(lista)
listm = [2, 3, 1, 5, 7]
print(sorted(listm))
print(lista.sort())
print(lista)
listc.sort(reverse=True)
print(sorted(lista, reverse = True))
'''
num = [43, 78, 21, 96]
num.sort(reverse=True)
print(num)
num.sort()
print(num)