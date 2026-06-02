def popper(a_list):
    while a_list:
        popped_value = a_list.pop()
        print("list after popping: ",popped_value, a_list)
    print(a_list)
def main():
    sample_list = [10, 20, 30, 40, 50]
    popper(sample_list)
if __name__ == "__main__":
    main()            