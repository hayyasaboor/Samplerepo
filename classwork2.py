def extender(a_list, b_list):
    a_list += b_list
    return a_list
def main():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    extended_list = extender(list1, list2)
    print("Extended list: ", extended_list)
if __name__ == "__main__":
    main()    
